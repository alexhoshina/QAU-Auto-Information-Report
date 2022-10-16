import requests

# 这是上报类，用于执行与上报相关的操作，包括了获取登录所需的key，登录，上报，获取问卷情况等
# 其中的请求头均为最简单的请求头，没有添加任何额外的信息，甚至标准的User-Agent等信息没有，可根据需要自行添加
class Reports():
    def __init__(self):
        self.Login_api = 'https://zhxg.qau.edu.cn/xuegong/api/UserAuth/GetManUserLogin' # 这是登录的api
        self.Key_api = 'https://zhxg.qau.edu.cn/xuegong/api/BaseData/GetAuthCode' # 这是获取key的api
        self.Report_api  = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/AddVirus' # 这是进行上报的api
        self.Logout_api = 'https://zhxg.qau.edu.cn/xuegong/api/UserAuth/UserLoginOut' #这是登出的api
        self.Qnr_api = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/GetYesterdayData' # 这是获取问卷的api
        self.header = {'Content-Type': 'application/json;charset=UTF-8','Accept': 'application/json'} # 通用请求头
        self.cookie = {"insert_cookie":"29594869"} # 通用cookie
    def GetKey(self):
        # 获取key
        return requests.post(self.Key_api, headers=self.header)
    def Login(self,username,userpassword,key):
        # 登录智慧学工,获取token
        data = {
            'LoginName':username,
            'Pwd': userpassword,
            'key': key,
            'ApplyType': 1,
        }
        return requests.post(self.Login_api, headers=self.header, json=data)

    def Report(self,token,content):
        # 进行上报
        header = {
            'X-Token': token,
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json'
        }
        return requests.post(self.Report_api, headers=header, cookies=self.cookie, data=content.encode("utf-8"))

    def Logout(self,token):
        # 登出智慧学工
        headers = {
            'x-token': token,
            'content-type': 'application/json',
            'Accept': 'application/json'
        }
        return requests.get(self.Logout_api, headers=headers)

    def GetQnr(self,token):
        # 获取问卷情况
        headers = {
                'Accept': 'application/json',
                'X-Token': token,
            }
        return requests.get(self.Qnr_api, headers=headers, cookies=self.cookie)