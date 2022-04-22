import requests
import re
import time
import json

<<<<<<< HEAD
=======
#模式选择，数值为0或1，目前仅1模式可用
model = 1

>>>>>>> 567cc0cd48d9a4444506c7da6dc24d73b816bdbe
Time = time.strftime("%Y-%m-%d", time.localtime())
get_key_url = 'https://zhxg.qau.edu.cn/xuegong/api/BaseData/GetAuthCode'
get_token_url = 'https://zhxg.qau.edu.cn/xuegong/api/UserAuth/GetManUserLogin'
get_data_url = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/GetYesterdayData'
enter_url = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/AddVirus'

requests.get(get_key_url,get_token_url, verify=False)
requests.get(enter_url,get_data_url, verify=False)

<<<<<<< HEAD
with open('config.json','r', encoding='UTF-8') as f:
    User = json.load(f)
    
with open('config.json','r', encoding='UTF-8') as f:
    data = json.load(f)
    data['NowDate'] = '%s'%(Time)
=======
User = {
    'username' : 'your name',
    'userpassword' : 'your password',
    'cookies' : {'your cookies'},
    'NowDate' : '%s'%(Time),
    'Country': '中国',
    'Province':'山东省',
    'City':'青岛市',
    'County':'平度市',
    'street_number':'海信路',
    'CurrentPosition':'中国山东省青岛市平度市海信路',
    # 您第一针疫苗接种时间，请严格遵守下格式
    'FirstStitchDate':'xxxx-xx-xx',
    # 您第二针疫苗接种时间，请严格遵守下格式
    'TwoStitchDate':'xxxx-xx-xx'
}    
>>>>>>> 567cc0cd48d9a4444506c7da6dc24d73b816bdbe

#获取key
def get_key():
    key_origin = requests.post(get_key_url,  cookies=User['cookies'])
    key_0 = re.search(r'Key...(.{36})', key_origin.text)
    return key_0.group(1)

#获取X-Token
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

<<<<<<< HEAD
def get_data(token,Time,data):
    if(User['model']):
        del data['username']
        del data['cookies']
        del data['userpassword']
        del data['model']
        print(data)
        data_str = json.dumps(data,ensure_ascii=False)
        print(data_str)
=======
#上报数据获取模块，分为1模式（预设模式）和0模式（昨日模式），目前昨日模式存在无法解决的bug，请勿使用。（由变量model控制模式）
def get_data(token,Time):
    if(model):
        data = '{"NowDate":"%s","UserType":1,"Country":"%s","Province":"%s","City":"%s","County":"%s","street_number":"%s","CurrentPosition":"%s","FirstStitchDate":"%s","TwoStitchDate":"%s","ThreeStitchDate":null,"TodaySchedule":0,"BRHGTJZRSFYXLQKOne":0,"BRHGTJZRSFYXLQKTwo":0,"SZSQTNSFFSYQ":0,"LJSHJCS":0,"BRHGTJZRSFYYXZZWQY":0,"JRSFCSWFL":0,"JRSFCSNQTDJSFQ":0,"DayTemperature":1,"Vaccination":2,"Remark":""}'%(User['NowDate'],User['Country'],User['Province'],User['City'],User['County'],User['street_number'],User['CurrentPosition'],User['FirstStitchDate'],User['TwoStitchDate'])
>>>>>>> 567cc0cd48d9a4444506c7da6dc24d73b816bdbe
    else:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'X-Token': token,
        }
        data_0 = requests.get(get_data_url, headers=headers, cookies=User['cookies'])
        print(data_0.text)
        data = data_0.text
        data = re.sub(r'"NowDate":null', '"NowDate":"%s"'%Time, data)
<<<<<<< HEAD
        data = re.sub(r'"County":""', '"County":"%s","CurrentPosition":"%s"'%(User['County'],User['CurrentPosition']), data)
        data_str = re.search(r'({"Id".+)',data).group(1)
    return data_str
=======
    return data
>>>>>>> 567cc0cd48d9a4444506c7da6dc24d73b816bdbe

#上报模块
def enter(data,token):
    headers = {
    'X-Token': token,
    'Content-Type': 'application/json;charset=UTF-8',
    }
    response = requests.post(enter_url, headers=headers, cookies=User['cookies'], data=data.encode("utf-8"))
    response.enconding="utf-8"
    print('\n\n%s' % response.text)

<<<<<<< HEAD
enter(get_data(get_token(get_key(),User['username'],User['userpassword']),User['NowDate'],data),get_token(get_key(),User['username'],User['userpassword']))
=======
#运行上报
enter(get_data(get_token(get_key(),User['username'],User['userpassword']),User['NowDate']),get_token(get_key(),User['username'],User['userpassword']))
>>>>>>> 567cc0cd48d9a4444506c7da6dc24d73b816bdbe
