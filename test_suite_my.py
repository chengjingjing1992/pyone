#coding=utf-8
import unittest
from test_user_login import TestUserLogin
from test_user_getinfo import TestUserGetInfo
from test_user_getArticleType import TestUserArticle
suite=unittest.TestSuite()
suite.addTest(TestUserLogin('test_user_login_normal')) # 添加单个用例
suite.addTest(TestUserGetInfo('test_b_user_getInfo'))
suite.addTest(TestUserGetInfo('test_c_user_getUnreadMessageNum'))
suite.addTest(TestUserArticle('test_user_getArticleType'))
unittest.TextTestRunner(verbosity=2).run(suite)  # verbosity显示级别，运行顺序为添加到suite中的顺序