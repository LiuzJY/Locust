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
            "channel": "12",
            "version": "6.7.4",
            "ua": "Android_migu",
            "msisdn": data['msisdn'],
            "uid": data['uid'],
            "logId": "MIGUTEST",
            "IMEI": "99999999999999999999",
            "idfa": "99999999999999999999"
        }
        return headers

    # @task(1)
    # h5保存用户问卷信息
    def saveAnswer(self):
        url = "/MAC/activity3/model/offline/saveAnswer"
        params = {"activityId": "MAC_SCANCODE_GY_MB_CSHD",
                  "answer": "1231"}
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

    # @task(1)
    # h5查询是否获取过幸运码
    def isGotLuckyCode(self):
        url = "/MAC/activity3/model/offline/isGotLuckyCode"
        params = {"activityId": "MAC_SCANCODE_GY_MB_CSHD"}
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

    # @task(1)
    # h5获取幸运码
    def getLuckyCode(self):
        url = "/MAC/activity3/model/offline/getLuckyCode"
        params = {"activityId": "MAC_SCANCODE_GY_MB_CSHD"}
        with self.client.get(url, params=params, headers=MyTaskSet.on_start(self), catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    # @task(1)
    # www确认中奖用户接口
    def savePrizeUsers(self):
        url = "/MAC/activity3/model/offline/savePrizeUsers"
        params = {"channel": "12",
                  "activityId": "MAC_SCANCODE_GY_MB_CSHD",
                  "msisdns": "15825297843",
                  "batch": "1",
                  "seq": "123456",
                  "k": "qwertyuiopasdfghjklzxcvbnmqwerty",
                  "v": "D8B1D47A3FD0F1D0C353FF3D46A65489"}
        with self.client.get(url, params=params, catch_response=True)as response:
            print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    # @task(1)
    # www获取中奖用户列表接口
    def getPrizeUsers(self):
        url = "/MAC/activity3/model/offline/getPrizeUsers"
        params = {"channel": "12",
                  "activityId": "MAC_SCANCODE_GY_MB_CSHD",
                  "batch": "1",
                  "seq": "123456",
                  "k": "qwertyuiopasdfghjklzxcvbnmqwerty",
                  "v": "3C87401F830B611D5E84C04BEF059056"}
        with self.client.get(url, params=params, catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    # @task(1)
    # www获取参与用户列表接口
    def getJoinUsers(self):
        url = "/MAC/activity3/model/offline/getJoinUsers"
        params = {"channel": "12",
                  "activityId": "MAC_SCANCODE_GY_MB_CSHD",
                  "pageNum": "1",
                  "seq": "123456",
                  "k": "qwertyuiopasdfghjklzxcvbnmqwerty",
                  "v": "A244AF939E08752C12F869F9ECD759AD"}
        with self.client.get(url, params=params, catch_response=True)as response:
            print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    @task(1)
    # www获取预中奖用户列表接口
    def getFakePrizeUsers(self):
        url = "/MAC/activity3/model/offline/getFakePrizeUsers"
        params = {"channel": "12",
                  "activityId": "MAC_SCANCODE_GY_MB_CSHD",
                  "seq": "123456",
                  "k": "qwertyuiopasdfghjklzxcvbnmqwerty",
                  "v": "158A0415BAA8FD21E4BE887E89952646"}
        with self.client.get(url, params=params, catch_response=True)as response:
            print(response.text)
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
    os.system("locust -f XXSM.py --host=http://app.act.nf.migu.cn")
