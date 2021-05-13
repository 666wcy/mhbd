# -*- coding: utf-8 -*-
import  json
import requests
import re
import time
session = requests.Session()
username=''
password=''

if __name__ == '__main__':
    header = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 5.4; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",

    }
    url='https://www.manhuabudang.com/index.php'        #主页面地址
    html=requests.get(url,headers=header)
    #开始获取模拟登陆需要的post数据-step
    step=re.findall("<input type=\"hidden\" name=\"step\" value=\"(.*?)\" />", html.text, re.S)[0]

    data={
        'pwuser':username.encode("GBK"),
        'pwpwd':password,
        'cktime':'3600',
        'jumpurl':'https://www.manhuabudang.com/index.php',
        'step':step,
        'question': '0',
        'customquest':'',
        'answer':'',
        'head_login':'',
        'lgt': '0'

    }
    loginurl='https://www.manhuabudang.com/login.php?'
    login=session.post(loginurl,headers=header,data=data)


    adminurl='https://www.manhuabudang.com/u.php'
    admin=session.get(adminurl,headers=header)
    #print(admin.text)

    step1=re.findall("<input type=\"hidden\" name=\"step\" value=\"(.)\">", admin.text, re.S)[0]
    print(step1)
    verify=re.findall("<input type=\"hidden\" name=\"verify\" value=\"(.*?)\">", admin.text, re.S)[0]

    print(verify)
    data1={
        'step':step1
    }
    nowtime=int(round(time.time() * 1000))
    endurl='https://www.manhuabudang.com/jobcenter.php?action=punch&nowtime=%s&verify=%s&verify=%s'%(nowtime,verify,verify)
    end=session.post(endurl,headers=header,data=data1)
    print(end.text)
