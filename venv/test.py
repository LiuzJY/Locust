import requests
# from locust import HttpLocust, TaskSet, task
# import queue
import random
#
#
url = "http://10.25.246.28:18089/MAC/activity3/model/v2.0/queryMyPrizeList"
params = {"activityId": "MAC_LHX_KF_DRHLC",
          "activityType": "1"}
headers = {"channel": "014000D",
           "version": "5.0.1",
           "ua": "Android_migu"}

res = requests.get(url, params=params, headers=headers)
# res = requests.post(url, data=params, headers=headers)
print(res.json())
# #
# # f = open("C:/Users/admin/Desktop/123.txt")
# # lines = f.readlines()
# # print(lines)
# # print("////////////////////////////////////////////////////////")
# # for line in lines:
# #     # print(line)
# #     # print(line.split(",")[0])
# #     # print(line.split(",")[1])
# #     msisdn = line.split(",")[0]
# #     uid = line.rstrip('\n').split(",")[1]
# #     headers = {
# #         "channel": "014000D",
# #         "version": "5.0.1",
# #         "ua": "Android_migu",
# #         "msisdn": msisdn,
# #         "uid": uid,
# #         "logId": "MIGUTEST",
# #         "IMEI": "99999999999999999999",
# #         "idfa": "99999999999999999999"
# #     }
# #     print(headers)
# #     res = requests.post(url, data=params, headers=headers)
# #     print(res.json())
#
#
# class MyTaskSet(TaskSet):
#
#     # headers = {"channel": "014000D",
#     #            "version": "5.0.1",
#     #            "ua": "Android_migu"}
#
#     @task(1)
#     def test(self):
#         url = "/MAC/activity3/qgdxyyls2019/querySingersByType"
#         params = {"activityId": "QGDXYYLS2019",
#                   "activityStage": "1",
#                   "singerType": "3",
#                   "queryType": "search",
#                   "page": "1",
#                   "singerName": "周"}
#         global data
#         try:
#             data = self.locust.queueData.get_nowait()  # 获取队列里的数据
#             print(data)
#         except queue.a:  # 队列取空后，直接退出
#             print('no data exist')
#             exit(0)
#
#         print('actually msisdn and uid is {} and {}'.format(data['msisdn'], data['uid']))
#         headers = {
#             "channel": "014000D",
#             "version": "5.0.1",
#             "ua": "Android_migu",
#             "msisdn": data["msisdn"],
#             "uid": data["uid"],
#             "logId": "MIGUTEST",
#             "IMEI": "99999999999999999999",
#             "idfa": "99999999999999999999"
#         }
#         with self.client.get(url, headers=headers, params=params, catch_response=True)as response:
#             print(response.text)
#             # print(response.content)
#             if response.status_code == 200:
#                 print("success")
#                 # response.failure(headers["msisdn"])
#             assert 'success' in response.text, "Respense error: " + response
#
#
# class MyLocust(HttpLocust):
#     task_set = MyTaskSet
#     queueData = queue.Queue()
#     f = open("../123.txt")
#     lines = f.readlines()
#     print(lines)
#     for line in lines:
#         msisdn = line.split(",")[0]
#         uid = line.rstrip('\n').split(",")[1]
#         data = {
#             "msisdn": msisdn,
#             "uid": uid
#         }
#         queueData.put_nowait(data)
#     max_wait = 3000
#     min_wait = 1000
#
#
# if __name__ == "__main__":
#     import os
#     os.system("locust -f test.py --host=http://10.25.246.28:18089")
#
#
#
#
#
#
#
# np.random.choice(range(1,self.sides+1),10,p=[1/self.sides]*self.sides)).to_list()
#
# sides = 5
# a = random.choice(range(1, sides+1),10)
# print(a)