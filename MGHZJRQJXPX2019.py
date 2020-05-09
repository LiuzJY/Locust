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
            "version": "6.7.4",
            "ua": "Android_migu",
            "msisdn": data['msisdn'],
            "uid": data['uid'],
            "logId": "MIGUTEST",
            "IMEI": "99999999999999999999",
            "idfa": "99999999999999999999"
        }
        return headers

    # @task(15)
    # 查询福袋状态接口
    def queryMiguCoinOpenState(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryMiguCoinOpenState"
        params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
                  "activityStage": "1"}
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

    # @task(5)
    # 查询用户票卡详情接口
    def queryDcardConsumeList(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryDcardConsumeList"
        params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
                  "queryType": "1",
                  "pageNum": "1"}
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

    @task(5)
    # 查询真爱粉丝榜单1
    def queryTopVoterList1(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryTopVoterList?activityId=MAC_ZP_KF_MGHZJRQJXPX2019&activityStage=1" \
              "&singerId=1000021316&queryType=1"
        # params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
        #           "activityStage": "1",
        #           "queryType": "1",
        #           "singerId": "1000021316"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    @task(5)
    # 查询真爱粉丝榜单2
    def queryTopVoterList2(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryTopVoterList?activityId=MAC_ZP_KF_MGHZJRQJXPX2019&activityStage=1" \
              "&singerId=1000000616&queryType=1"
        # params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
        #           "activityStage": "1",
        #           "queryType": "1",
        #           "singerId": "1000000616"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    @task(5)
    # 查询真爱粉丝榜单3
    def queryTopVoterList3(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryTopVoterList?activityId=MAC_ZP_KF_MGHZJRQJXPX2019&activityStage=1" \
              "&singerId=1001060006&queryType=1"
        # params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
        #           "activityStage": "1",
        #           "queryType": "1",
        #           "singerId": "1001060006"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    @task(5)
    # 查询真爱粉丝榜单4
    def queryTopVoterList4(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryTopVoterList?activityId=MAC_ZP_KF_MGHZJRQJXPX2019&activityStage=1" \
              "&singerId=99&queryType=1"
        # params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
        #           "activityStage": "1",
        #           "queryType": "1",
        #           "singerId": "99"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    @task(5)
    # 查询真爱粉丝榜单5
    def queryTopVoterList5(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryTopVoterList?activityId=MAC_ZP_KF_MGHZJRQJXPX2019&activityStage=1" \
              "&singerId=1002043559&queryType=1"
        # params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
        #           "activityStage": "1",
        #           "queryType": "1",
        #           "singerId": "1002043559"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    @task(5)
    # 查询真爱粉丝榜单6
    def queryTopVoterList6(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryTopVoterList?activityId=MAC_ZP_KF_MGHZJRQJXPX2019&activityStage=1" \
              "&singerId=356&queryType=1"
        # params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
        #           "activityStage": "1",
        #           "queryType": "1",
        #           "singerId": "356"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    @task(5)
    # 查询真爱粉丝榜单7
    def queryTopVoterList7(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryTopVoterList?activityId=MAC_ZP_KF_MGHZJRQJXPX2019&activityStage=1" \
              "&singerId=1001060006&queryType=1"
        # params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
        #           "activityStage": "1",
        #           "queryType": "1",
        #           "singerId": "1001060006"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    @task(5)
    # 查询真爱粉丝榜单8
    def queryTopVoterList8(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryTopVoterList?activityId=MAC_ZP_KF_MGHZJRQJXPX2019&activityStage=1" \
              "&singerId=529&queryType=1"
        # params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
        #           "activityStage": "1",
        #           "queryType": "1",
        #           "singerId": "529"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    @task(5)
    # 查询真爱粉丝榜单9
    def queryTopVoterList9(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryTopVoterList?activityId=MAC_ZP_KF_MGHZJRQJXPX2019&activityStage=1" \
              "&singerId=1106691172&queryType=1"
        # params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
        #           "activityStage": "1",
        #           "queryType": "1",
        #           "singerId": "1106691172"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    @task(1)
    # 查询真爱粉丝榜单10
    def queryTopVoterList10(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryTopVoterList?activityId=MAC_ZP_KF_MGHZJRQJXPX2019&activityStage=1" \
              "&singerId=1000002548&queryType=1"
        # params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
        #           "activityStage": "1",
        #           "queryType": "1",
        #           "singerId": "1000002548"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    @task(1)
    # 查询真爱粉丝榜单11
    def queryTopVoterList11(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryTopVoterList?activityId=MAC_ZP_KF_MGHZJRQJXPX2019&activityStage=1" \
              "&singerId=1212&queryType=1"
        # params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
        #           "activityStage": "1",
        #           "queryType": "1",
        #           "singerId": "1212"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    @task(3)
    # 查询真爱粉丝榜单12
    def queryTopVoterList12(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryTopVoterList?activityId=MAC_ZP_KF_MGHZJRQJXPX2019&activityStage=1" \
              "&singerId=1000008439&queryType=1"
        # params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
        #           "activityStage": "1",
        #           "queryType": "1",
        #           "singerId": "1000008439"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    @task(50)
    # 查询打CALL歌手排行榜接口
    def querySingerRankingList(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/querySingerRankingList?activityId=MAC_ZP_KF_MGHZJRQJXPX2019" \
              "&activityStage=1"
        # params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
        #           "activityStage": "1"}
        with self.client.get(url, headers=MyTaskSet.on_start(self), catch_response=True)as response:
            # print(response.text)
            if float(response.elapsed.total_seconds()) > 1:
                # print(response.text)
                response.failure("response timeout 1s：" + str(response.elapsed.total_seconds()))
            if response.text.find("\"code\":\"199999\"") > 0:
                # print(response.text)
                response.failure("code is 199999")
            else:
                response.success()

    # @task(10)
    # 查询我的排名（某歌手下）接口
    def queryMyVoteInfo(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryMyVoteInfo"
        params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
                  "activityStage": "1",
                  "singerId": "1001060006"}
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

    # @task(20)
    # 查询当前阶段详情接口
    def queryActivityStage(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryActivityStage"
        params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019"}
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
    # 升级提示语接口
    def querySystemUpgradeInfo(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/querySystemUpgradeInfo"
        params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019"}
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

    # @task(10)
    # 查询投票渠道是否关闭
    def queryVoteChannelClose(self):
        url = "/MAC/activity3/mghzjrqjxpx2019/queryVoteChannelClose"
        params = {"activityId": "MAC_ZP_KF_MGHZJRQJXPX2019",
                  "activityStage": "1"}
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
    os.system("locust -f MGHZJRQJXPX2019.py --host=http://app.act.nf.migu.cn")
