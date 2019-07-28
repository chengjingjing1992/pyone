#coding=utf-8
import unittest
import requests
import test_globle
class TestUserArticle(unittest.TestCase):

    def test_user_getArticleType(self):
        url="http://servemobiletest.kuaishouax.com/ApiAjax/GetArticleType"
        #从全局变量拿值
        userid=test_globle.userId
        params={
            "userid":userid
        }
        r=requests.request("post",url,params=params)
        dic=r.json()

        self.assertEqual(dic["code"],0)
        self.assertEqual(dic["successful"],True)