# -*- coding:utf-8 -*-
import io
from locust import HttpLocust, TaskSet, task
try:
    import queue
except ImportError:
    import Queue as queue


class MyTaskSet(TaskSet):

    def on_start(self):
        global data
        try:
            data = self.locust.queueData.get_nowait()
            # print("++++++++++++++++++++++++++++++++++++++++++++++++++")
            # print("获取队列data:%s" % data)
        except queue.Empty:
            print("no data")
            exit(0)
        # print('actually msisdn and uid is {} and {}'.format(data['msisdn'], data['uid']))
        self.locust.queueData.put(data)
        headers = {
            "channel": "123",
            "version": "123",
            "ua": "123",
            "msisdn": data['msisdn'],
            "uid": data['uid'],
            "logId": "123",
            "IMEI": "123",
            "idfa": "123"
        }
        return headers

    # @task(15)
    # 查询福袋状态接口
    def queryMiguCoinOpenState(self):
        url = "/url/123/123/123"
        params = {"activityId": "123",
                  "activityStage": "123"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), params=params, catch_response=True)as response:
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
    host = "http://www.123.com"
    queueData = queue.Queue(maxsize=100)
    with io.open("123.txt", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            msisdn = line.split(",")[0]
            uid = line.rstrip('\n').split(",")[1]
            data = {
                "msisdn": msisdn,
                "uid": uid
            }
            queueData.put(data)


if __name__ == "__main__":
    import os
    os.system("locust -f queueTest.py --host=http://www.123.com")

