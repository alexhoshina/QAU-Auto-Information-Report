import requests
import re
import time

Time = time.strftime("%Y-%m-%d", time.localtime())
cookies = {'your cookies'}
cookies_1 = {'insert_cookies in your cookies'}
username = 'your username'
userpassword = 'your password'
data = '{"NowDate":"%s","UserType":1,"Country":"中国","Province":"山东省","City":"青岛市","County":"平度市","street_number":"海信路","CurrentPosition":"中国山东省青岛市平度市海信路","FirstStitchDate":"your Time","TwoStitchDate":"your Time","ThreeStitchDate":null,"TodaySchedule":0,"BRHGTJZRSFYXLQKOne":0,"BRHGTJZRSFYXLQKTwo":0,"SZSQTNSFFSYQ":0,"LJSHJCS":0,"BRHGTJZRSFYYXZZWQY":0,"JRSFCSWFL":0,"JRSFCSNQTDJSFQ":0,"DayTemperature":1,"Vaccination":2,"Remark":""}'%(Time)
#！！！！！！！！后滑填写疫苗接种时间！！！！！！！                                                                                                                                                                                 #这是第一针接种时间            #这是第二针接种时间
def get_key():
   url='https://zhxg.qau.edu.cn/xuegong/api/BaseData/GetAuthCode'
   headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://zhxg.qau.edu.cn',
    'Referer': 'https://zhxg.qau.edu.cn/zhxg/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
   requests.get(url, verify=False)
   r = requests.post(url, headers=headers, cookies=cookies)
   key = r.text
   a = re.search(r'Key...(.{36})', key)
   key_0 = a.group(1) 
   return key_0

def get_token(key_0,username,userpassword):
    url='https://zhxg.qau.edu.cn/xuegong/api/UserAuth/GetManUserLogin'
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'DNT': '1',
    'Origin': 'https://zhxg.qau.edu.cn',
    'Referer': 'https://zhxg.qau.edu.cn/zhxg/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }
    json_data = {
    'LoginName': username,
    'Pwd': userpassword,
    'key': 'key_0',
    'ApplyType': 1,
}
    requests.get(url, verify=False)
    response = requests.post(url, headers=headers, cookies=cookies, json=json_data)
    token = response.text
    print(token)
    a = re.search(r'Token":"(.+)","E', token)
    token_0 = a.group(1) 
    return token_0

def enter(data,token):
    url = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/AddVirus'
    headers = {
    'Host': 'zhxg.qau.edu.cn',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'X-Token': token,
    'AppType': '2#3.0.0#1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MIX 2S Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3171 MMWEBSDK/20211202 Mobile Safari/537.36 MMWEBID/5331 MicroMessenger/8.0.18.2062(0x28001241) Process/appbrand2 WeChat/arm64 Weixin GPVersion/1 NetType/4G Language/zh_CN ABI/arm64 miniProgram/wx9af32b509e88340c',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://zhxg.qau.edu.cn',
    'X-Requested-With': 'com.tencent.mm',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://zhxg.qau.edu.cn/xgwui/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    requests.get(url, verify=False)
    response = requests.post(url, headers=headers, cookies=cookies_1, data=data.encode("UTF-8"))
    response.enconding="utf-8"
    print(response.text)

enter(data,get_token(get_key(),username,userpassword))