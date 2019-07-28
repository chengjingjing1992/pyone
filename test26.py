# #coding=utf-8
# #python 接口测试
import requests

import json


url="http://servemobiletest.kuaishouax.com/ApiLogin/AjaxUserLogin"
params={
    "userType":"1",
    "telphone":"13585658502",
    "password":"123456"
}
r=requests.request("post",url,params=params)
print(r.text)
requests.post(url,params,)


