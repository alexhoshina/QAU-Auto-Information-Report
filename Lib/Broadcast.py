import time
import requests

# 这是广播类，用于执行与广播相关的操作，包括了调用Server酱进行广播，在本地存储Log，可自行添加其他广播方式。
class Broadcast():
    def __init__(self,case1 = 'null',case2 = 'null',qnr = 'null'):
        self.case1 = case1 # 运行状态
        self.case2 = case2 # 上报状态
        self.qnr   = qnr   # 问卷情况
        self.time:str  = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())# 获取当前时间
    def __str__(self):
        # 重写str方法，方便输出
        msg  = '\n运行时间:\n\t'
        msg += self.time
        msg += '\n运行状态:\n\t'
        msg += self.case1
        msg += '\n上报状态:\n\t'
        msg += self.case2
        msg += '\n问卷情况:\n\t'
        msg += self.qnr
        msg += '     \n\n     '
        return msg
    def Server(self,ServerKey):
        # 调用server酱进行通知
        data = {'title': '每日上报情况通知','desp': self}
        requests.post('https://sctapi.ftqq.com/'+ServerKey, params=data)
    def Log(self):
        # 在本地保存日志
        try:
            # 写入日志    
            with open('log.txt', 'a', encoding='UTF-8') as f:
                f.write(self.__str__())
        except FileNotFoundError:
            # 如果没有log.txt文件，则创建
            with open('log.txt', 'a', encoding='UTF-8') as f:
                f.write(self.__str__())