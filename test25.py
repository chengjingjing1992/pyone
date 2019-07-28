#coding=utf-8
# 什么是装饰器？
# 定义了一个函数想在运行时增加功能，又不想改动函数本身的代码
# 装饰器可以简化代码 及日志  数据库事务
def new_f(f):
    def fn(x):
        print("555")
        return f(x)
    return fn

@new_f
def f1(x):
    return (x*x)

print(f1(3))
# g=new_f(f1)
# print(g(8))











def fun_new(f):
    def fn(x):
        print("log......")
        return f(x)
    return fn

@fun_new
def fun(x):
    return x*2

# 装饰器函数


# n=fun_new(fun)
# a=n(12)
# print(a)

# fun=fun_new(fun)
# print(fun(12))

print(fun(15))


































