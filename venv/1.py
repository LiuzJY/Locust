from locust import HttpLocust, TaskSet, task


class MyTaskSet(TaskSet):
    headers = {"channel": "014000D",
               "version": "5.0.1",
               "ua": "Android_migu",
               "msisdn": "13541353607",
               "uid": "37a64160-421a-4935-936b-4709710bc316",
               "logId": "MIGUTEST",
               "IMEI": "99999999999999999999",
               "idfa": "99999999999999999999"}

    @task(1)
    # 查询我的排名
    def queryMyRankByAct(self):
        url = "/MAC/activity3/areavote/queryMyRankByAct"
        params = {"activityId": "LDZY2019",
                  "singerId": "1004252240",
                  "stage": "1"}
        with self.client.get(url, headers=MyTaskSet.headers, params=params, catch_response=True)as response:
            print("查询我的排名："+response.text)
            if int(response.elapsed.total_seconds()) > 2:
                response.failure("response timeout 2s")
            if response.text.find("\"code\":\"000000\"") < 1:
                response.failure("code is not 000000")
            else:
                response.success()

    @task(1)
    # 查询榜单
    def queryRankListByAct(self):
        url = "/MAC/activity3/areavote/queryRankListByAct"
        params = {"activityId": "LDZY2019",
                  "stage": "1"}
        with self.client.get(url, headers=MyTaskSet.headers, params=params, catch_response=True)as response:
            print("查询榜单"+response.text)
            if int(response.elapsed.total_seconds()) > 2:
                response.failure("response timeout 2s")

            if response.text.find("\"code\":\"000000\"") < 1:
                response.failure("code is not 000000")
            else:
                response.success()

    @task(1)
    # 查询贡献榜
    def queryContributeListByAct(self):
        url = "/MAC/activity3/areavote/queryContributeListByAct"
        params = {"activityId": "LDZY2019",
                  "singerId": "1004252240",
                  "stage": "1"}
        with self.client.get(url, headers=MyTaskSet.headers, params=params, catch_response=True)as response:
            print("查询贡献榜"+response.text)
            if int(response.elapsed.total_seconds()) > 2:
                response.failure("response timeout 2s")

            if response.text.find("\"code\":\"000000\"") < 1:
                response.failure("code is not 000000")
            else:
                response.success()

    @task(1)
    # 查询福袋领取资格
    def queryLuckyBagStatus(self):
        url = "/MAC/activity3/areavote/queryLuckyBagStatus"
        params = {"activityId": "HITOMUSIC"}
        with self.client.get(url, headers=MyTaskSet.headers, params=params, catch_response=True)as response:
            print("查询领取资格"+response.text)
            if int(response.elapsed.total_seconds()) > 2:
                response.failure("response timeout 2s")

            if response.text.find("\"code\":\"000000\"") < 1:
                response.failure("code is not 000000")
            else:
                response.success()

    # @task(1)
    # 领取福袋
    def getLuckyBag(self):
        url = "/MAC/activity3/areavote/getLuckyBag"
        params = {"activityId": "HITOMUSIC",
                  "token": "111",
                  "passId": "111"}
        with self.client.get(url, headers=MyTaskSet.headers, params=params, catch_response=True)as response:
            print("领取福袋"+response.text)
            if int(response.elapsed.total_seconds()) > 2:
                response.failure("response timeout 2s")

            if response.text.find("\"code\":\"000000\"") < 1:
                response.failure("code is not 000000")
            else:
                response.success()

    # @task(1)
    # 外部渠道投票
    def voteSinger(self):
        url = "/MAC/activity3/areavote/voteSinger"
        params = {"activityId": "LDZY2019",
                  "singerId": "1002152545",
                  "count": "10",
                  "sign": "0a5ea4e00d891dfa30b3a49649d6740f"}  # sign为md5加密，需要根据手机号+渠道+投票数+歌手id+密钥生成
        with self.client.get(url, headers=MyTaskSet.headers, params=params, catch_response=True)as response:
            print("外部渠道投票"+response.text)
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


if __name__ == "__main__":
    import os
    os.system("locust -f HitoVsCallNight.py --host=http://app.act.nf.migu.cn")
