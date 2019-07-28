#coding=utf-8
import unittest
import requests
import test_globle
from http.cookiejar import CookieJar,LWPCookieJar
from urllib.request import Request,urlopen,HTTPCookieProcessor,build_opener
class TestUserLogin(unittest.TestCase):
    # # 生成一个管理cookie的对象
    # cookies = CookieJar()
    # # 创建一个支持cookie的对象，对象属于HTTPCookieProcessor
    # cookie_handler = HTTPCookieProcessor(cookies)
    # # 创建一个opener
    # opener = build_opener(cookie_handler)

    def test_user_login_normal(self):# 一条测试用例，必须test_开头

        url="http://servemobiletest.kuaishouax.com/ApiLogin/AjaxUserLogin"
        params={
            "userType":"1",
            "telphone":"13585658502",
            "password":"123456"
        }

        r=requests.request("post",url,params=params)
        # 设置全局变量
        test_globle.requestsCookieJar = r.cookies
        self.assertIn("true",r.text) # 断言






    def test_user_login_wrongPwd(self):
        url = "http://servemobiletest.kuaishouax.com/ApiLogin/AjaxUserLogin"
        params = {
            "userType": "1",
            "telphone": "13585658502",
            "password": "123000"
        }
        r = requests.request("post", url, params=params)
        print(r.text)
        self.assertIn("false", r.text)  # 断言

        def setUpModule():
            print("所有模块执行之前用次方法")

    if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
        unittest.main(verbosity=2)  # 运行本测试类所有用例,verbosity为结果显示级别


