# -*- coding:utf-8 -*-
import io
from locust import HttpLocust, TaskSet, task
try:
    import queue
except ImportError:
    import Queue as queue


class MyTaskSet(TaskSet):
    # headers = {"channel": "014000D",
    #            "version": "5.0.1",
    #            "ua": "Android_migu",
    #            "msisdn": "13541353607",
    #            "uid": "37a64160-421a-4935-936b-4709710bc316",
    #            "logId": "MIGUTEST",
    #            "IMEI": "99999999999999999999",
    #            "idfa": "99999999999999999999"}

    # def on_start(self):
    #     global data
    #     try:
    #         data = self.locust.queueData.get_nowait()
    #         # print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    #         # print("获取队列data:%s" % data)
    #     except queue.Empty:
    #         print("no data")
    #         exit(0)
    #     # print('actually msisdn and uid is {} and {}'.format(data['msisdn'], data['uid']))
    #     self.locust.queueData.put(data)
    #     params = {
    #         "activityId": "MAC_ZY_KF_MGHXCCJ",
    #         "userMsisdn": data['msisdn']
    #     }
    #     return params

    @task(1)
    # www获取预中奖用户列表接口
    def getFakePrizeUsers(self):
        url = "/MAC/activity3/mghxccj/wapSyncMsisdn"
        headers = {"channel": "014000D",
                   "version": "5.0.1",
                   "ua": "Ios_migu",
                   "logId": "MIGUTEST",
                   "IMEI": "99999999999999999999",
                   "idfa": "99999999999999999999"}
        params = {
            "activityId": "MAC_ZY_KF_MGHXCCJ",
            "userMsisdn": "13426160830"
        }
        with self.client.get(url, params=params, headers=headers,  catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1
    max_wait = 3
    host = "http://10.25.151.17"
    # queueData = queue.Queue(maxsize=100)
    # with io.open("123.txt", encoding="utf-8") as file:
    #     while True:
    #         line = file.readline()
    #         if not line:
    #             break
    #         msisdn = line.split(",")[0]
    #         uid = line.rstrip('\n').split(",")[1]
    #         data = {
    #             "msisdn": msisdn,
    #             "uid": uid
    #         }
    #         queueData.put(data)


if __name__ == "__main__":
    import os
    os.system("locust -f MGHXCCJ.py --host=http://app.act.nf.migu.cn")
