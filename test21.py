#coding=utf-8
# filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，
# 这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
#
# 例如，要从一个list [1, 4, 6, 7, 9, 12, 17]中删除偶数，保留奇数，首先，要编写一个判断奇数的函数：
#
# def is_odd(x):
#     return x % 2 == 1
# 然后，利用filter()过滤掉偶数：
#
# filter(is_odd, [1, 4, 6, 7, 9, 12, 17])
# 结果：[1, 7, 9, 17]




# Python内置的 sorted()函数可对list进行排序：
#
# >>>sorted([36, 5, 12, 9, 21])
#
# [5, 9, 12, 21, 36]
#
# 但 sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，比较函
# 数的定义是，传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。
#
# 因此，如果我们要实现倒序排序，只需要编写一个reversed_cmp函数：
#
# def reversed_cmp(x, y):
#     if x > y:
#         return -1
#     if x < y:
#         return 1
#     return 0
# 这样，调用 sorted() 并传入 reversed_cmp 就可以实现倒序排序：
#
# >>> sorted([36, 5, 12, 9, 21], reversed_cmp)
# [36, 21, 12, 9, 5]