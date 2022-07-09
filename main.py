import requests
import time
import json
import datetime
import pytz

class origin():
    def __init__(self):
        self.key_api = 'https://zhxg.qau.edu.cn/xuegong/api/BaseData/GetAuthCode'
        self.token_api  = 'https://zhxg.qau.edu.cn/xuegong/api/UserAuth/GetManUserLogin'
        self.Qnr_api  = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/GetYesterdayData'
        self.data_api  = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/GetVirusBaseList'
        self.enter_api  = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/AddVirus'
        self.Server_api  = 'https://sctapi.ftqq.com/%s'%(self.User()['Server'])
        self.User = self.User()
        self.data_dict = self.data_dict()
    def User(self):
        with open('User.json','r', encoding='UTF-8') as f:
            User = json.load(f)
        return User
    def data_dict(self):
        with open('config.json','r', encoding='UTF-8') as f:
                data_dict = json.load(f)
        Time = datetime.datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime(' %Y-%m-%d ')
        data_dict['NowDate'] = '%s'%(Time)
        return data_dict

class shangbao(origin):
    def __init__(self):
        origin.__init__(self)
        self.key = self.key_get()
        self.token = self.token_get()
        self.data = self.data_get()
        self.enter = self.enter_start()
    def key_get(self):
        key0 = requests.post(self.key_api, cookies=self.data_dict['cookies'], verify=False).json()
        key1 = json.dumps(key0)
        key = json.loads(key1)
        return key['ResultValue']['Key']
    def token_get(self):
        json_data = {
            'LoginName': self.User['username'],
            'Pwd': self.User['userpassword'],
            'key': self.key,
            'ApplyType': 1,
        }
        token0 = requests.post(self.token_api, cookies=self.data_dict['cookies'], json=json_data, verify=False).json()
        token1 = json.dumps(token0)
        token = json.loads(token1)
        return token['ResultValue']['Token']
    def data_get(self):
        if(self.User['model'] == '1'):#data_config
           data = json.dumps(self.data_dict,ensure_ascii=False)
        else:#data_origin
            pass
        return data
    def enter_start(self):
        headers = {
        'X-Token': self.token,
        'Content-Type': 'application/json;charset=UTF-8',
        }
        enter0 = requests.post(self.enter_api, headers=headers, cookies=self.data_dict['cookies'], data=self.data.encode("utf-8"), verify=False).json()
        enter1 = json.dumps(enter0)
        enter = json.loads(enter1)
        return enter

class tongzhi():
    def Qnr(self):
        headers = {
                'Accept': 'application/json, text/plain, */*',
                'X-Token': ShangBao.token,
            }
        Qnr0 = requests.get(ShangBao.Qnr_api, headers=headers, cookies=ShangBao.data_dict['cookies'], verify=False).json()
        Qnr1 = json.dumps(Qnr0)
        Qnr = json.loads(Qnr1)
        return Qnr['ResultValue']
    def Estimate(self):
        if(ShangBao.enter['RequestMsg'] == ''):
            Tz = '上报已成功'
        elif(ShangBao.enter['RequestMsg'] == '今日您已经上报，无需重复上报'):
            Tz = '今日已成功上报'
        else:
            Tz = '上报未成功，请手动上报.\n以下内容为返回信息\nRequestMsg: %s'%(ShangBao.enter['RequestMsg'])
        return Tz
    def Server(self):
        data = {
        'title': '每日上报情况通知',
        'desp': '上报状态:\n%s\n\n上报问卷情况:\n %s'%(self.Estimate(),self.Qnr()),
        }
        requests.post(ShangBao.Server_api, params=data)

if (__name__ == '__main__'):
    ShangBao = shangbao()
    if (ShangBao.User['Server_on-off'] == '1'):
        TongZhi = tongzhi()
        TongZhi.Server()