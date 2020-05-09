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

    # @task(1)
    # 兑换码兑换数字专辑接口
    def exchangeAlbum(self):
        url = "/MAC/activity3/model/code/exchangeAlbum"
        params = {"activityId": "MAC_LJ_KF_NPCSZZJDH",
                  "code": "1004252240"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), params=params, catch_response=True)as response:
            # print("兑换码兑换数字专辑："+response.text)
            if int(response.elapsed.total_seconds()) > 2:
                response.failure("response timeout 2s")
            if response.text.find("\"code\":\"000000\"") < 1:
                response.failure("code is not 000000")
            else:
                response.success()

    # @task(1)
    # 图册登记邮寄地址接口
    def queryContributeListByAct(self):
        url = "/MAC/activity3/model/v2.0/recordUserSendInfo"
        params = {"activityId": "MAC_LJ_KF_NPCSZZJDH",
                  "activityType": "0",
                  "username": "用户名称",
                  "contact": "11111111111",
                  "address": "四川省成都市高新区中海国际J座5楼",
                  "identityId": "5112554649191651651",
                  "identityType": "1",
                  "prizeId": "奖品id",
                  "sessionId": "中奖信息的唯一标识	"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), params=params, catch_response=True)as response:
            # print("图册登记邮寄地址接口" + response.text)
            if int(response.elapsed.total_seconds()) > 2:
                response.failure("response timeout 2s")

            if response.text.find("\"code\":\"000000\"") < 1:
                response.failure("code is not 000000")
            else:
                response.success()

    @task(1)
    # 查询专辑销量接口
    def querySalesVolume(self):
        url = "/MAC/activity3/npcszzjdh/querySalesVolume"
        params = {"activityId": "MAC_LJ_KF_NPCSZZJDH"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), params=params, catch_response=True)as response:
            # print(MyTaskSet.on_start(self))
            # print("查询专辑销量接口"+response.text)
            if int(response.elapsed.total_seconds()) > 2:
                response.failure("response timeout 2s")

            if response.text.find("\"code\":\"000000\"") < 1:
                response.failure("code is not 000000"+response.text)
            else:
                response.success()

    # @task(1)
    # 查询剩余图册数量接口
    def queryRestNum(self):
        url = "/MAC/activity3/npcszzjdh/queryRestNum"
        params = {"activityId": "MAC_LJ_KF_NPCSZZJDH"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), params=params, catch_response=True)as response:
            # print("查询剩余图册数量接口"+response.text)
            if int(response.elapsed.total_seconds()) > 2:
                response.failure("response timeout 2s")

            if response.text.find("\"code\":\"000000\"") < 1:
                response.failure("code is not 000000")
            else:
                response.success()

    # @task(1)
    # 查询个人中奖记录接口
    def queryMyPrizeList(self):
        url = "/MAC/activity3/model/v2.0/queryMyPrizeList"
        params = {"activityId": "MAC_LJ_KF_NPCSZZJDH",
                  "activityType": "0"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), params=params, catch_response=True)as response:
            # print("查询个人中奖记录接口"+response.text)
            if int(response.elapsed.total_seconds()) > 2:
                response.failure("response timeout 2s")

            if response.text.find("\"code\":\"000000\"") < 1:
                response.failure("code is not 000000")
            else:
                response.success()

    # @task(1)
    # 查询我的积分接口
    def queryMyPoints(self):
        url = "/MAC/activity3/npcszzjdh/queryMyPoints"
        params = {"activityId": "MAC_LJ_KF_NPCSZZJDH"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), params=params, catch_response=True)as response:
            # print("查询我的积分接口"+response.text)
            if int(response.elapsed.total_seconds()) > 2:
                response.failure("response timeout 2s")

            if response.text.find("\"code\": \"000000\"") < 1:
                response.failure("code is not 000000")
            else:
                response.success()

    # @task(1)
    # 积分兑换图册接口
    def exchangePrize(self):
        url = "/MAC/activity3/npcszzjdh/exchangePrize"
        params = {"activityId": "MAC_LJ_KF_NPCSZZJDH",
                  "num": "1"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), params=params, catch_response=True)as response:
            # print("积分兑换图册接口"+response.text)
            if int(response.elapsed.total_seconds()) > 2:
                response.failure("response timeout 2s")

            if response.text.find("\"code\":\"000000\"") < 1:
                response.failure("code is not 000000")
            else:
                response.success()


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 3000
    queueData = queue.Queue(maxsize=100)
    with io.open("../123.txt", encoding="utf-8") as file:
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
            # print(data)


if __name__ == "__main__":
    import os
    os.system("locust -f NPCSZZJDH.py --host=http://10.25.246.28:18089")
