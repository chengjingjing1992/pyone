#coding=utf-8
import unittest
from test_user_login import TestUserLogin
from test_user_getinfo import TestUserGetInfo
suite=unittest.TestSuite()
suite.addTest(TestUserLogin('test_user_login_normal')) # 添加单个用例
suite.addTest(TestUserGetInfo('test_b_user_getInfo'))
unittest.TextTestRunner(verbosity=2).run(suite)  # verbosity显示级别，运行顺序为添加到suite中的顺序