#coding=utf-8
def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum

# 像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。
# 闭包的特点是返回的函数还引用了外层函数的局部变量
# 所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。