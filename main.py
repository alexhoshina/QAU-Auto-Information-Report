import sys
from Content import *
from Reports import *
from Broadcast import *
def check_key(dict, key,name,user=None):
    if key in dict:
        return dict[key]
    else:
        try:
            sys.exit()
        except SystemExit:
            broadcast = Broadcast()
            broadcast.case1 = '运行失败,在获取%s时出错'%(name)
            broadcast.Server(user['ServerKey'])
            broadcast.Log()
            sys.exit()

def main():
    # 创建对象
    content = Content()
    reports = Reports()
    broadcast = Broadcast()
    # 获取用户信息
    user = content.GetUser()
    # 获取预设上报信息
    config = content.GetConfig()
    # 获取key
    key = reports.GetKey()
    key = check_key(key, 'Key','key',user)
    # 登录
    login = reports.Login(user['username'],user['userpassword'],key)
    # 获取token
    token = check_key(login.json(), 'Token','token',user)
    # 获取问卷
    qnr = reports.GetQnr(token)
    qnr = check_key(qnr.json(), 'ResultValue','qnr',user)
    # 上报
    report = reports.Report(token,config)
    # 获取上报结果
    result = check_key(report.json(), 'ResultValue','result',user)
    if (result == ''):
        result = '上报成功'
    else:
        result = result
    # 登出
    logout = reports.Logout(token)
    # 创建广播内容
    broadcast.case1 = '运行成功'
    broadcast.case2 = result
    broadcast.qnr = qnr
    # 发送广播
    broadcast.Server(user['ServerKey'])
    broadcast.Log()

if __name__ == "__main__":
    main()
