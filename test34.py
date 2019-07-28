#coding=utf-8
# 如何让每个实例拥有各自不同的属性？由于Python是动态语言，对每一个实例
# ，都可以直接给他们的属性赋值，例如，给xiaoming这个实例加上name、gender和birth属性：
class Person():
    pass

xiaoming=Person();
xiaoming.name="xiaoming"
xiaoming.age=24
print(xiaoming.name)
print(xiaoming.age)
