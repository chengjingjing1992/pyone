#coding=utf-8
# 2.1
# 函数式编程简介
# 高阶函数;函数可以作为变量传入 ,能接收函数作为参数的函数即高阶函数
# 闭包:可以返回函数

# 2.2

# abs是函数取绝对值
b=abs
c=b(-2)
print(c)



# 写个高阶函数两个数的绝对值相加

# def add(x,y,f):
#     return f(x)+f(y)
#
# f=abs
#
# d=add(-3,-4,f)
# print(d)
#


#求两个数的开方之和
import math


# def add(x, y, f):
#     return f(x) + f(y)
#
# def squre(n):
#     return math.pow(n,0.5)
#
# f=squre
# print(add(9,25,f))


# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
def f(x):
    return x*x

list=map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in list:
    print(i)










