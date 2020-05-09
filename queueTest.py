from locust import HttpLocust, TaskSet, task
import queue


class MyTaskSet(TaskSet):
    # headers = {"channel": "014000D",
    #            "version": "5.0.1",
    #            "ua": "Android_migu",
    #            "msisdn": "13541353607",
    #            "uid": "37a64160-421a-4935-936b-4709710bc316",
    #            "logId": "MIGUTEST",
    #            "IMEI": "99999999999999999999",
    #            "idfa": "99999999999999999999"}
    def on_start(self):
        global data
        try:
            data = self.locust.queueData.get_nowait()
            print("++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("获取队列data:%s" % data)
        except queue.Empty:
            print("no data")
            exit(0)
        print('actually msisdn and uid is {} and {}'.format(data['msisdn'], data['uid']))
        self.locust.queueData.put(data)
        headers = {
            "channel": "014000D",
            "version": "5.0.1",
            "ua": "Android_migu",
            "msisdn": data['msisdn'],
            "uid": data['uid'],
            "logId": "MIGUTEST",
            "IMEI": "99999999999999999999",
            "idfa": "99999999999999999999"
        }
        return headers

    @task(1)
    # 查询我的排名
    def queryMyRankByAct(self):
        url = "/MAC/activity3/areavote/queryMyRankByAct"
        params = {"activityId": "LDZY2019",
                  "singerId": "1004252240",
                  "stage": "1"}
        headers = MyTaskSet.on_start(self)
        with self.client.get(url, headers=headers, params=params, catch_response=True)as response:
            print("查询我的排名："+response.text)
            print("请求中的msisdn:"+response.request.headers['msisdn'])
            print("使用的msisdn:"+headers["msisdn"])
            if int(response.elapsed.total_seconds()) > 2:
                response.failure("response timeout 2s")
            if response.text.find("\"code\":\"000000\"") < 1:
                response.failure("code is not 000000")
            else:
                response.success()


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    queueData = queue.Queue(maxsize=100)
    f = open("123.txt")
    lines = f.readlines()
    for line in lines:
        msisdn = line.split(",")[0]
        uid = line.rstrip('\n').split(",")[1]
        data = {
            "msisdn": msisdn,
            "uid": uid
        }
        print(data)
        queueData.put(data)


if __name__ == "__main__":
    import os
    os.system("locust -f queueTest.py --host=http://app.act.nf.migu.cn")
