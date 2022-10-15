import json
import time

class Content():
    def __init__(self) :
        self.Qnr_api = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/GetYesterdayData' # 这是获取问卷的api
    def GetUser(self):
        # 读取用户信息
        with open('User.json','r', encoding='UTF-8') as f:
                user = json.load(f)
        return user
    def GetConfig(self) :
        # 读取预设的上报信息
        with open('config.json','r', encoding='UTF-8') as f:
                config = json.load(f)
        # 提供日期
        config['NowDate'] = '%s'%(time.strftime("%Y-%m-%d", time.localtime()))
        config = json.dumps(config,ensure_ascii=False) 
        return config