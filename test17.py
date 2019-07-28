#coding=utf-8
# 请定义Person类的__init__方法，除了接受 name、gender 和 birth 外，还可接受任意关键字参数，并把他们都作为属性赋值给实例。
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


xiaoming=person("xiaoming",25)
print(xiaoming.name)