#coding=utf8
# 演示定义一个函数
def hello():
    print("hello...")

hello()


# 演示默认参数



# 演示不定长参数


#演示 匿名函数  python 使用 lambda 来创建匿名函数。
numbers = [1, 3, 6]
newNumbers = tuple(map(lambda x: x , numbers))
print(newNumbers)