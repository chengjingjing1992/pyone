#coding=utf-8
import unittest
import requests
import test_user_login
from http.cookiejar import CookieJar,LWPCookieJar
from requests.cookies import RequestsCookieJar
import test_globle
class TestUserGetInfo(unittest.TestCase):


    # def test_a_user_loginNormal(self):
    #     url = "http://servemobiletest.kuaishouax.com/ApiLogin/AjaxUserLogin"
    #     params = {
    #         "userType": "1",
    #         "telphone": "13585658502",
    #         "password": "123456"
    #     }
    #     r = requests.request("post", url, params=params)
    #     # 设置全局变量
    #     test_globle.requestsCookieJar=r.cookies
    #
    #     self.assertIn("true",r.text) # 断言



    def test_b_user_getInfo(self):
        url="http://servemobiletest.kuaishouax.com/ApiAccount/PersonalInfo"
        requestsCookieJar=test_globle.requestsCookieJar
        r=requests.request("post",url,cookies=requestsCookieJar)
        print(type(r.text))

        dic=r.json()#返回的是字典格式
        print(type(dic["code"]))
        self.assertEqual(0,dic["code"])# 断言接口返回的code 值是否为0