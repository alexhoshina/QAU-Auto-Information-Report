# 变量名 xxxx_origin 通常代表post后取得的原始数据，一般需要经过截取处理后才能使用

#初始化库
import requests
import re
import time
import json

#获取当前日期，并存入Time变量中
Time = time.strftime("%Y-%m-%d", time.localtime())

#提交post中所用到的链接
get_key_url = 'https://zhxg.qau.edu.cn/xuegong/api/BaseData/GetAuthCode'
get_token_url = 'https://zhxg.qau.edu.cn/xuegong/api/UserAuth/GetManUserLogin'
get_data_url = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/GetYesterdayData'
enter_url = 'https://zhxg.qau.edu.cn/xuegong/api/DayVirus/AddVirus'

#关闭所有连接的证书验证
requests.get(get_key_url,get_token_url, verify=False)
requests.get(enter_url,get_data_url, verify=False)

#取得配置文件内的配置
with open('config.json','r', encoding='UTF-8') as f:
    User = json.load(f)
#取得配置文件内配置 
with open('config.json','r', encoding='UTF-8') as f:
    data = json.load(f)
    #为配置文件内的NowDate提供数据
    data['NowDate'] = '%s'%(Time)
#

#获取key
def get_key():
    key_origin = requests.post(get_key_url,  cookies=User['cookies'])
    #利用正则提取出key值，这个正则式等待优化
    key = re.search(r'Key...(.{36})', key_origin.text)
    return key.group(1)

#获取X-token
def get_token(key,username,userpassword):
    json_data = {
    'LoginName': '%s'%(username),
    'Pwd': '%s'%(userpassword),
    'key': '%s'%(key),
    'ApplyType': 1,
    }
    token_origin = requests.post(get_token_url,  cookies=User['cookies'], json=json_data)
    #利用正则提取出token值
    token = re.search(r'Token":"(.+)","E', token_origin.text)
    return token.group(1)

#获取信息上报的数据
def get_data(token,Time,data):
    if(User['model']):
        #预设模式

        #删除多余的不必要键与键值
        del data['username']
        del data['cookies']
        del data['userpassword']
        del data['model']
        #将字典变量转为字符串
        data_str = json.dumps(data,ensure_ascii=False)
    else:
        #获取昨日数据模式，此模式无法取得街道信息和定位信息，故使用预设中的参数值
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'X-Token': token,
        }
        data_origin = requests.get(get_data_url, headers=headers, cookies=User['cookies'])
        data = data_origin.text
        #利用正则填补所获取的Data数据中所缺失的部分
        data = re.sub(r'"NowDate":null', '"NowDate":"%s"'%Time, data)
        data = re.sub(r'"County":""', '"County":"%s","CurrentPosition":"%s"'%(User['County'],User['CurrentPosition']), data)
        #将字典变量转为字符串
        data_str = re.search(r'({"Id".+)',data).group(1)
    return data_str

#上报模块
def enter(data,token):
    headers = {
    'X-Token': token,
    'Content-Type': 'application/json;charset=UTF-8',
    }
    response = requests.post(enter_url, headers=headers, cookies=User['cookies'], data=data.encode("utf-8"))
    response.enconding="utf-8"
    #打印上报后的信息
    print('\n\n%s' % response.text)

#调用上报模块函数
enter(get_data(get_token(get_key(),User['username'],User['userpassword']),User['NowDate'],data),get_token(get_key(),User['username'],User['userpassword']))