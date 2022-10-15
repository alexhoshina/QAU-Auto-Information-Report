import time
import requests

class Broadcast():
    def __init__(self,case1 = 'null',case2 = 'null',qnr = 'null'):
        self.case1 = case1
        self.case2 = case2
        self.qnr   = qnr
        self.time:str  = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    def __str__(self):
        msg  = '\n运行时间:\n\t'
        msg += self.time
        msg += '\n运行状态:\n\t'
        msg += self.case1
        msg += '\n上报状态:\n\t'
        msg += self.case2
        msg += '\n问卷情况:\n\t'
        msg += self.qnr
        return msg
    def Server(self,ServerKey):
        # 调用server酱进行通知
        data = {'title': '每日上报情况通知','desp': self}
        requests.post('https://sctapi.ftqq.com/'+ServerKey, params=data)
    def Log(self):
        # 在本地保存日志
        try:    
            with open('log.txt', 'a', encoding='UTF-8') as f:
                f.write(self.__str__())
        except FileNotFoundError:
            with open('log.txt', 'a', encoding='UTF-8') as f:
                f.write(self.__str__())