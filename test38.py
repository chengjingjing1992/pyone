#coding=utf-8
class Person(object ):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod  #类方法
    def sayName(cls):  #类方法的第一个参数将传入类本身，通常将参数名命名为 cls
        print("sayName()")
        pass


Person.sayName()