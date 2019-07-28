#coding=utf-8
from http.cookiejar import CookieJar,LWPCookieJar
from urllib.request import Request,urlopen,HTTPCookieProcessor,build_opener
from urllib.parse import urlencode
import ssl
import requests


url="http://servemobiletest.kuaishouax.com/ApiLogin/AjaxUserLogin"
params={
            "userType":"1",
            "telphone":"13585658502",
            "password":"123456"
}

r=requests.request("post",url,params=params)
print(r.text)
cookie_obj=r.cookies
print(type(cookie_obj))
personalInfoUrl="http://servemobiletest.kuaishouax.com/ApiAccount/PersonalInfo"
r=requests.request("post",personalInfoUrl,cookies=cookie_obj)
print(r.text)