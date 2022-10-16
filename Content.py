import json
import time

# 这个类用于读取配置文件，其中配置文件的格式为json，路径为/*，需要与主程序放在同一目录下 
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
        # 将上报信息转换为json格式
        config = json.dumps(config,ensure_ascii=False) 
        return config