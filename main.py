import requests
import re
import time
import json

Time = time.strftime("%Y-%m-%d", time.localtime())
get_key_url = 'https://zhxg.qau.edu.cn/xuegong/api/BaseData/GetAuthCode'
get_token_url = 'https://zhxg.qau.edu.cn/xuegong/api/UserAuth/GetManUserLogin'
get_data_url = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/GetYesterdayData'
enter_url = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/AddVirus'

requests.get(get_key_url,get_token_url, verify=False)
requests.get(enter_url,get_data_url, verify=False)

with open('config.json','r', encoding='UTF-8') as f:
    User = json.load(f)
    
with open('config.json','r', encoding='UTF-8') as f:
    data = json.load(f)
    data['NowDate'] = '%s'%(Time)

def get_key():
    key_origin = requests.post(get_key_url,  cookies=User['cookies'])
    key_0 = re.search(r'Key...(.{36})', key_origin.text)
    return key_0.group(1)

def get_token(key,username,userpassword):
    json_data = {
    'LoginName': '%s'%(username),
    'Pwd': '%s'%(userpassword),
    'key': '%s'%(key),
    'ApplyType': 1,
    }
    token_origin = requests.post(get_token_url,  cookies=User['cookies'], json=json_data)
    token_0 = re.search(r'Token":"(.+)","E', token_origin.text)
    return token_0.group(1)

def get_data(token,Time,data):
    if(User['model']):
        del data['username']
        del data['cookies']
        del data['userpassword']
        del data['model']
        print(data)
        data_str = json.dumps(data,ensure_ascii=False)
        print(data_str)
    else:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'X-Token': token,
        }
        data_0 = requests.get(get_data_url, headers=headers, cookies=User['cookies'])
        print(data_0.text)
        data = data_0.text
        data = re.sub(r'"NowDate":null', '"NowDate":"%s"'%Time, data)
        data = re.sub(r'"County":""', '"County":"%s","CurrentPosition":"%s"'%(User['County'],User['CurrentPosition']), data)
        data_str = re.search(r'({"Id".+)',data).group(1)
    return data_str

def enter(data,token):
    headers = {
    'X-Token': token,
    'Content-Type': 'application/json;charset=UTF-8',
    }
    response = requests.post(enter_url, headers=headers, cookies=User['cookies'], data=data.encode("utf-8"))
    response.enconding="utf-8"
    print('\n\n%s' % response.text)

enter(get_data(get_token(get_key(),User['username'],User['userpassword']),User['NowDate'],data),get_token(get_key(),User['username'],User['userpassword']))