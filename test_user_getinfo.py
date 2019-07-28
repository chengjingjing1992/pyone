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
        # 从全局变量获取cookie
        requestsCookieJar=test_globle.requestsCookieJar
        r=requests.request("post",url,cookies=requestsCookieJar)
        dic=r.json()#返回的是字典格式
        self.assertEqual(0,dic["code"])# 断言接口返回的code 值是否为0
        # 给全局变量 userid 赋值
        test_globle.userId=dic["data"]["shopUser"]["UserID"]



    def test_c_user_getUnreadMessageNum(self):
        url="http://servemobiletest.kuaishouax.com/ApiAccount/GetUnreadMessageNum"
        # 从全局变量获取cookie
        requestsCookieJar = test_globle.requestsCookieJar
        # 发送请求
        r = requests.request("post", url, cookies=requestsCookieJar)
        # 返回的是字典格式
        dic = r.json()
        # 断言接口返回的code 值是否为0
        self.assertEqual(0,dic["code"])

        self.assertEqual(dic["successful"],True)


