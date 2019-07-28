# #coding=utf-8
# # Python对属性权限的
# # 控制是通过属性名来实现的，如果一个属性由双下划线开头(__)，该属性就无法被外部访问。
#
# # 以单下划线开头的属性"_xxx"虽然也可以被外部访问，但是，按照习惯，他们不应该被外部访问。
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#         self._title = 'Mr'
#         self.__job = 'Student'
#
# p = Person('Bob')
# print (p.name)
# print(p._title)
# print(p.__job)