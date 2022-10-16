import sys
from Content import *
from Reports import *
from Broadcast import *

# 对获取到的字典进行判断，判断是否获取到了预期的key，并提取出key
def check_key(dict, key,name,user=None):
    # 由于获取到的字典中均包含ResultValue，所以可以通过判断ResultValue是否存在来初步判断是否获取到了预期的key
    if 'ResultValue' in dict.keys():
        dict = dict['ResultValue'] # 如果获取到的字典里包含ResultValue，则将字典中的ResultValue提取出来  
        # 通过key进一步判断是否获取到了预期的key
        if key in dict.keys():
            # 如果获取到的字典中包含预期的key，则将key提取出来
            return dict[key]
        else:
            # 如果获取到的字典中不包含预期的key，则退出程序，并进行广播
            try:
                sys.exit()
            except SystemExit:
                broadcast = Broadcast()
                broadcast.case1 = '运行失败,在获取%s时出错'%(name)
                broadcast.Server(user['ServerKey'])
                broadcast.Log()
                sys.exit()
    else:
        # 如果获取到的字典中不包含ResultValue，则退出程序，并进行广播
        try:
            # 对sys.exit()抛出的异常进行捕获，以便进行sys.exit()后的操作
            sys.exit()
        except SystemExit:
            # 在捕获到异常后，进行广播，并退出程序
            broadcast = Broadcast()
            broadcast.case1 = '运行失败,在获取%s时出错'%(name)
            broadcast.Server(user['ServerKey'])
            broadcast.Log()
            sys.exit()

# 对上报所返回的信息进行判断，判断是否上报成功
def check_msg(dict,name,user=None):
    # 上报所返回信息存储在RequestMsg中，所以可以通过判断RequestMsg是否存在来初步判断是否上报成功
    if 'RequestMsg' in dict.keys():
        msg = dict['RequestMsg'] # 如果存在RequestMag，则将RequestMsg提取出来
        if msg == '':
            # 如果RequestMsg为空，则上报成功
            return '上报成功'
        else:
            # 如果RequestMsg不为空，则上报失败，返回RequestMsg
            return msg
    else:
        # 与获取key时一样，如果不存在RequestMsg，则退出程序，并进行广播
        try:
            sys.exit()
        except SystemExit:
            broadcast = Broadcast()
            broadcast.case1 = '运行失败,在获取%s时出错'%(name)
            broadcast.Server(user['ServerKey'])
            broadcast.Log()
            sys.exit()

# 对获取到的问卷进行判断，判断是否获取到了预期的问卷，并提取出问卷
def check_qnr(dict,name,user=None):
    # 问卷存储在ResultValue中，所以可以通过判断ResultValue是否存在来初步判断是否获取到了问卷
    if 'ResultValue' in dict.keys():
        qnr = dict['ResultValue'] # 如果存在ResultValue，则将ResultValue提取出来 
        if 'LoginName' in qnr.keys():
            # 如果获取到的问卷中包含LoginName，则说明获取到了问卷
            if qnr['LoginName'] == user['username']:
                # 如果获取到的问卷中的LoginName与预设的LoginName相同，则说明获取到了正确的问卷
                # 由于获取到的问卷中包含了问卷的所有信息，所以可以直接返回问卷
                # 但是返回的问卷为字典类型，所以需要将问卷转换为字符串类型
                return str(qnr)
            else:
                # 如果获取到的问卷中的LoginName与预设的LoginName不同，则说明获取到了错误的问卷
                return '问卷不正确'
        else:
            # 如果获取到的问卷中不包含LoginName，则说明获取到的不是问卷
            return '问卷获取失败'
    else:
        # 与获取key时一样，如果不存在ResultValue，则退出程序，并进行广播
        try:
            sys.exit()
        except SystemExit:
            broadcast = Broadcast()
            broadcast.case1 = '运行失败,在获取%s时出错'%(name)
            broadcast.Server(user['ServerKey'])
            broadcast.Log()
            sys.exit()

#  主函数，用于调用上述函数和导入的包
def main():
    # 创建对象，广播对象并未进行初始化
    content = Content()# 用于获取问卷内容
    reports = Reports()# 上报对象，无需初始化
    broadcast = Broadcast()# 广播对象，需要在更靠后的地方进行初始化，也可以在更靠后的地方进行创建
    # 获取用户信息
    user = content.GetUser()
    # 获取预设上报信息
    config = content.GetConfig()
    # 获取key
    key = reports.GetKey()
    # 判断key是否获取成功，若获取成功则对其进行提取，若获取失败则退出程序
    key = check_key(key.json(), 'Key','key',user)
    # 传入username和userpwd和key，进行登录，若无key可能会导致登录失败
    login = reports.Login(user['username'],user['userpassword'],key)
    # 获取token，其本质是判断是否登录成功，若登录成功则对token进行提取，若登录失败则退出程序
    token = check_key(login.json(), 'Token','token',user)
    # 获取问卷，并对问卷进行处理
    qnr = reports.GetQnr(token)
    qnr = check_qnr(qnr.json(),'qnr',user)
    # 进行上报
    report = reports.Report(token,config)
    # 获取上报结果
    result = check_msg(report.json(),'result',user)
    # 登出，这里的登出是为了释放token
    logout = reports.Logout(token)
    # 创建广播内容，对未进行初始化的广播对象进行初始化
    broadcast.case1 = '运行成功' # 运行成功
    broadcast.case2 = result # 上报结果
    broadcast.qnr = qnr # 问卷内容
    # 发送广播
    broadcast.Server(user['ServerKey'])# 调用广播对象的Server方法，传入ServerKey
    broadcast.Log()# 在本地打印日志

# 用于判断是否是主程序
if __name__ == "__main__":
    # 调用主函数
    main()