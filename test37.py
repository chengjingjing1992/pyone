#coding=utf-8
# 绑定在一个实例上的属性不会影响其他实例，但是，类本身也是一个对象，
# 如果在类上绑定一个属性，则所有实例都可以访问类的属性，并且，
# 所有实例访问的类属性都是同一个！也就是说，实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。

class Person(object):
    address="earth" # 类属性
    def __init__(self,name):
        self.name=name


xiaoming=Person('xiaoming')
print(xiaoming.name)
# print(xiaoming.address)
print(Person.address)# 类属性

Person.address2="moon"
print(Person.address2)#类属性也是可以动态添加和修改的


