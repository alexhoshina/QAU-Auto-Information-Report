import requests
import re
import time
import json
import datetime
import pytz

def url():
    global get_key_url
    global get_token_url
    global get_Qnr_url
    global get_data_url
    global enter_url
    global Server_url
    get_key_url = 'https://zhxg.qau.edu.cn/xuegong/api/BaseData/GetAuthCode'
    get_token_url = 'https://zhxg.qau.edu.cn/xuegong/api/UserAuth/GetManUserLogin'
    get_Qnr_url = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/GetYesterdayData'
    get_data_url = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/GetVirusBaseList'
    enter_url = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/AddVirus'
    Server_url = 'https://sctapi.ftqq.com/%s'%(User['Server'])

def get_User():
    global User
    with open('User.json','r', encoding='UTF-8') as f:
        User = json.load(f)

def get_data_dict():
    global data_dict
    with open('config.json','r', encoding='UTF-8') as f:
            data_dict = json.load(f)
    Time = datetime.datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime(' %Y-%m-%d ')
        #为配置文件内的NowDate提供数据
    data_dict['NowDate'] = '%s'%(Time)

def get_key():
    global key
    key_origin = requests.post(get_key_url,  cookies=data_dict['cookies'], verify=False)
    #利用正则提取出key值
    key = re.search(r'"Key":"(.+)","I', key_origin.text).group(1)
 
def get_token():
    global token
    json_data = {
    'LoginName': '%s'%(User['username']),
    'Pwd': '%s'%(User['userpassword']),
    'key': '%s'%(key),
    'ApplyType': 1,
    }
    token_origin = requests.post(get_token_url,  cookies=data_dict['cookies'], json=json_data, verify=False)
    #利用正则提取出token值
    token = re.search(r'Token":"(.+)","E', token_origin.text).group(1)

def get_data():
    global data
    if(User['model'] == '1'):
        #data_config
        #将字典变量转为字符串
        data = json.dumps(data_dict,ensure_ascii=False)
    else:
        #data_origin
        headers = {'Accept': 'application/json, text/plain, */*',
                    'X-Token': '%s'%(token),
                    'AppType': '2#3.0.0#1',
                    'Content-Type': 'application/json;charset=UTF-8',
                }
        json_data = '{"PageSize":34,"PageIndex":4,"total":34,"UserInfo":"","Mobile":"","NowProvince":"","NowCity":"","ReportedStartTime":"2022-04-23 00:00:00","ReportedEndTime":"","UserType":1}'
        requests.get(get_data_url, verify=False)
        woshi = requests.post(get_data_url, headers=headers, cookies=data_dict['cookies'], data=json_data, verify=False).text
        print(woshi)

def get_Qnr():
    global Qnr
    headers = {
            'Accept': 'application/json, text/plain, */*',
            'X-Token': '%s'%(token),
        }
    Qnr_origin = requests.get(get_Qnr_url, headers=headers, cookies=data_dict['cookies'], verify=False)
    Qnr = Qnr_origin.text

def enter():
    global enter
    headers = {
    'X-Token': token,
    'Content-Type': 'application/json;charset=UTF-8',
    }
    enter = requests.post(enter_url, headers=headers, cookies=data_dict['cookies'], data=data.encode("utf-8"), verify=False)
    #enter.enconding="utf-8"
    print (enter.text)

def Server():
    data = {
    'title': '每日上报情况通知',
    'desp': '上报状态：\n%s \n\n上报问卷情况：\n %s'%(enter.text,Qnr),
    }
    se = requests.post(Server_url, params=data).text
    print(se)

def main():
    get_User()
    get_data_dict()
    url()
    get_key()
    get_token()
    get_Qnr()
    get_data()
    enter()
    if(User['Server_on-off'] == '1'):
        Server()
    else:
        print('server酱未开启')
main()