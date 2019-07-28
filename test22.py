#coding=utf-8
# Python的函数不但可以返回int、str、list、dict等数据类型，还可以返回函数！
def f():
    print ('call f()...')
    # 定义函数g:
    def g():
        print ('call g()...')
    # 返回函数g:
    return g

 # x指向函数g()
#
x=f()
x()