# QAU-Auto-Information-Report
## 简介
这个Python脚本用于实现青岛农业大学每日信息上报的自动化  
  
* 这个项目的初衷是用于自己练习Git与GitHub的使用，对于Python仅仅进行了简单的了解，代码很粗糙，许多语法和代码结构并不规范。  
* 如果您的防疫信息出现变动，请务必及时更改脚本中所对应的参数。

# 使用说明
* 使用前的准备工作  
1、Python3.9(此脚本由python3.9编写，其他版本未做测试)   
2、安装依赖库  
` pip install requests `  
` pip install pytz `  
3、利用git或github的下载代码zip功能取得代码  
4、打开config.json文件和user.json文件  
5、对其中的参数进行填写并保存     
* 运行脚本  
    * 直接运行main.py  
    * 利用windows的`任务计划程序`实现定时自动上报  
    * 将代码部署至腾讯云函数、阿里函数计算等`云函数服务平台`   

# 利用windows的`任务计划程序`实现定时自动上报  
* 这部分是介绍如何使用windows的`任务计划程序`实现自动上报

# 将代码部署至`云函数服务平台`  
* 这部分是介绍如何将代码部署至`云函数服务平台`  
    * 由于腾讯云函数(SCF)收费政策更改，本说明将以阿里函数计算(AliFC)为说明对象  

* 使用腾讯云函数请下载`SCF.zip`，阿里函数计算请下载`AliFC.zip`
1. 进入阿里函数计算官网 `https://fcnext.console.aliyun.com/overview`，登录后进入控制台。  
2. 点击左侧栏的`服务及函数`，然后点击`创建服务`。
        ![](https://github.com/alexhoshina/QAU-Auto-Information-Report/blob/main/Pictures/AliFC-1.png)  
3. 输入服务名称和描述(可留空)
        ![](https://github.com/alexhoshina/QAU-Auto-Information-Report/blob/main/Pictures/AliFC-2.png)  
4. 点击左侧栏的`函数管理`，然后点击`创建函数`。
        ![](https://github.com/alexhoshina/QAU-Auto-Information-Report/blob/main/Pictures/AliFC-3.png)  
5. 创建方式选择`从零创建`，运行环境选择`python`， 代码上传方式选择`通过ZIP包上传代码`，代码包选择下载好的`AliFC.zip`。
        ![](https://github.com/alexhoshina/QAU-Auto-Information-Report/blob/main/Pictures/AliFC-4.png)  
6. 触发器类型选择`定时触发器`，触发方式选择`指定时间`，时区选择`Asia/Shanghai(北京时间)`，指定一个时间后点击`创建`。
        ![](https://github.com/alexhoshina/QAU-Auto-Information-Report/blob/main/Pictures/AliFC-5.png)  
7. 等待在线IDE启动后，打开`config.json`和`user.json`对其参数进行填写，填写完毕后，点击右上角的`保存并部署`
        ![](https://github.com/alexhoshina/QAU-Auto-Information-Report/blob/main/Pictures/AliFC-6.png)



# 参数说明
## user.json  
* model     
    * 当前仅有预设模式可用   
    * 参数值： 0/1   
    * 参数说明： 这是模式选择参数，1为 ` 预设模式 ` 0为 ` 昨日模式 `   
    预设模式下将使用config.json中所设置的内容来作为上报的参数  
    昨日模式下将获取昨日的上报信息来作为上报参数（由于获取的昨日问卷与所提交问卷内容与格式相差甚远，所以目前是不可用状态）
* username  
    * 参数值：   
    * 参数说明：这个参数是您的学工号
* userpassword  
    * 参数值：  
    * 参数说明：这个参数是您在登录每日上报系统是所使用的密码  
* Server_on-off  
    * 参数值：0/1
    * 参数说明：Server酱开关，0为关闭，1为开启  
* Server   
    * 参数值：
    * 参数说明：Server key 这里填入您的Server key
## config.json
* cookies  
    * 参数值：   
    * 参数说明： cookies您无需获取也无需对其进行改动
* NowDate  
    * 参数值：  xxxx-xx-xx  
    * 参数说明： 这是上报的时间，无需填写，将会自动获取
* Country  
    * 参数值：  中国  
    * 参数说明： 这是您所在的国家
* Province  
    * 参数值：  山东省  
    * 参数说明： 这是您所在的省份
* City  
    * 参数值：  青岛市  
    * 参数说明： 这是您所在的市
* County  
    * 参数值：  平度市  
    * 参数说明： 这是您所在的县市区
* street_number  
    * 参数值：  街道（道路）  
    * 参数说明： 这是您所在的街道（道路），对于平度校区来说这个值为，海信路或朱诸路
* CurrentPosition  
    * 参数值：  中国山东省青岛市平度市海信路  
    * 参数说明： 这是您的微信定位地址，对于平度校区为如上值
* title  
    * 参数值：  地点  
    * 参数说明：此为新增参数，其值暂不明确知晓
* desc  
    * 参数值：  详细地点 
    * 参数说明：此为新增参数，其值暂不明确知晓
* FirstStitchDate  
    * 参数值：  xxxx-xx-xx  
    * 参数说明： 这是您第一针疫苗的接种日期（若未接种则留空）
* TwoStitchDate  
    * 参数值：  xxxx-xx-xx  
    * 参数说明： 这是您第二针疫苗的接种日期（若未接种则留空）
* ThreeStitchDate  
    * 参数值：  xxxx-xx-xx  
    * 参数说明： 这是您第三针疫苗的接种日期（若未接种则留空）
* Vaccination  
    * 参数值：  0/1/2/3  
    * 参数说明： 这是您的疫苗接种次数
* BRHGTJZRSFYXLQKOne  
    * 参数值：  0/1/2/3   
    * 参数说明： 本人或共同居住人是否有下列情况，0无，1确诊病例，2疑似病例，3无症状病例
* BRHGTJZRSFYXLQKTwo  
    * 参数值：  0/1/2/3/4   
    * 参数说明： 本人或共同居住人是否有下列情况,0无，1密接，2伴随，3中高风险地区人员，4封控区溢出人员
* SZSQTNSFFSYQ  
    * 参数值：  0/1   
    * 参数说明： 所在社区21天内是否发生疫情,0否，1是
* LJSHJCS  
    * 参数值：  0/1   
    * 参数说明： 旅居史或接触史,0否，1是
* BRHGTJZRSFYYXZZWQY  
    * 参数值：  0/1/2/3  
    * 参数说明： 本人或共同居住人是否有以下症状未痊愈,0无，1咳嗽或咽痛，2发热，3乏力肌肉酸痛胸闷
* JRSFCSWFL  
    * 参数值：  0/1  
    * 参数说明： 今日是否从外省反鲁,0否，1是
* JRSFCSNQTDJSFQ  
    * 参数值：  0/1  
    * 参数说明： 今日是否从省内其他地级市返青,0否，1是
* TodaySchedule  
    * 参数值：  0/1  
    * 参数说明： 今日行程,0无外出,1有
* DayTemperature  
    * 参数值：  0/1/2/3/4/5/6/7/8  
    * 参数说明： 今日体温,0 36以下，1、36-36.5，2、36.6-36.9，3、37-37.2，4、37.3-37.9，5、38-38.5，6、38.6-39，7、39-40，8、40以上
* Remark  
    * 参数值：  
    * 参数说明： 备注
* TodayScheduleOther  
    * 参数值：  
    * 参数说明： 外出具体行程，如无行程则留空 
* IsInSchool  
    * 参数值：  0/1
    * 参数说明： 此为新增参数，其值暂不明确知晓
* IsInSchoolOfDay
    * 参数值：  0/1
    * 参数说明： 今日是否在校，0否，1是
* ISNATDay
    * 参数值：  0/1/2
    * 参数说明： 今日是否进行核酸检测，0未检测，1校内检测，2校外检测  
  
# ToDo
* 学习GUI界面，添加可视化界面 

