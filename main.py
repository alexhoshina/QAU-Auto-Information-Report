import requests
import json
import time

# 这个类用于获取上报所需信息
class GetContent():
    def __init__(self) :
        self.DataList_api = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/GetVirusBaseList' #这是获取上报列表的api
        self.Qnr_api = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/GetYesterdayData' # 这是获取问卷的api
    def GetConfig(self) :
        #读取预设的上报信息
        with open('config.json','r', encoding='UTF-8') as f:
                config0 = json.load(f)
        # 提供日期
        config0['NowDate'] = '%s'%(time.strftime("%Y-%m-%d", time.localtime()))
        config = json.dumps(config0,ensure_ascii=False) 
        return config
    def GetLast(self) :
        pass
    def GetQnr(self,token) :
        headers = {
                'Accept': 'application/json, text/plain, */*',
                'X-Token': '%s'%(token),
            }
        qnr = requests.get(self.Qnr_api, headers=headers, cookies={"insert_cookie":"29594869"}).json()
        return qnr['ResultValue']

# 这个类用于执行上报动作
class DoReport():
    def __init__(self):
        self.Login_api = 'https://zhxg.qau.edu.cn/xuegong/api/UserAuth/GetManUserLogin' # 这是获取token的api
        self.Key_api = 'https://zhxg.qau.edu.cn/xuegong/api/BaseData/GetAuthCode' # 这是获取key的api
        self.Run_api  = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/AddVirus' # 这是进行发送的api
        self.Logout_api = 'https://zhxg.qau.edu.cn/xuegong/api/UserAuth/UserLoginOut' #这是登出的api
    def GetKey(self):
        # 获取key
        key = requests.post(self.Key_api).json()
        return key['ResultValue']['Key']
        
    def Login(self,username,userpassword,key):
        # 登录智慧学工,获取token
        json_data = {
            'LoginName':'%s'%(username) ,
            'Pwd': '%s'%(userpassword),
            'key': '%s'%(key),
            'ApplyType': 1,
        }
        login = requests.post(self.Login_api, json=json_data).json()
        return login['ResultValue']['Token']

    def Run(self,token,content):
        # 进行上报
        headers = {
            'X-Token': '%s'%(token),
            'Content-Type': 'application/json;charset=UTF-8',
        }
        run = requests.post(self.Run_api, headers=headers, cookies={"insert_cookie":"29594869"}, data=content.encode("utf-8")).json()
        if (run['RequestMsg'] == ''):
            return '上报成功'
        else:
            return run['RequestMsg']
        
    def Logout(self,token):
        # 登出智慧学工
        headers = {
            'x-token': '%s'%(token),
            'content-type': 'application/json'
        }
        out = requests.get(self.Logout_api, headers=headers).json()
        return out

# 这个类用于根据上报结果进行通知
class Broadcast():
    def __init__(self,ServerKey,Case,Qnr):
        self.Server_api  = 'https://sctapi.ftqq.com/%s'%(ServerKey) 
        self.case = Case
        self.qnr = Qnr
    def Server(self):
        # 调用server酱进行通知
        data = {
        'title': '每日上报情况通知',
        'desp': '上报状态:\n%s'%(self.case),
        }
        requests.post(self.Server_api, params=data)
    def Log(self):
        # 在本地保存日志
        log = '\n'
        log += u'运行时间：%s\n' % time.strftime("%Y-%m-%d", time.localtime())
        log += u'上报状态：\n\t%s\n' % self.case
        log += u'问卷内容：\n\t%s\n' % self.qnr
        log += u'\n' 
        try:    
            with open('log.txt', 'a', encoding='UTF-8') as f:
                f.write(log)
        except FileNotFoundError:
            with open('log.txt', 'a', encoding='UTF-8') as f:
                f.write(log)

if (__name__ == '__main__'):
    #读取用户设置
    with open('User.json','r', encoding='UTF-8') as f:
            User = json.load(f)
    #创建对象
    getcontent = GetContent()
    dorepore = DoReport()
#------------------------------进行上报------------------------------
    content = getcontent.GetConfig()
    key = dorepore.GetKey()
    token = dorepore.Login(User['username'],User['userpassword'],key)
    run = dorepore.Run(token,content)
    qnr = getcontent.GetQnr(token)
    out = dorepore.Logout(token)
#-------------------------------------------------------------------

#------------------------------进行通知------------------------------
    if (User['Log'] == '1' or User['Server'] == '1'):    
        #创建广播对象
        broadcast = Broadcast(User['ServerKey'],run,qnr)
        if (User['Log'] == '1'):
            #打印log
            broadcast.Log()
        else:
            pass    

        if (User['Server'] == '1'):
            #调用server酱
            broadcast.Server()
        else:
            pass 
#-------------------------------------------------------------------    