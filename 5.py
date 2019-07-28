#coding=utf-8
# 输入三个整数x,y,z，请把这三个数由小到大输出。
l=[]
for i in range(3):
    a=input("输入数字")
    l.append(a)

l.sort()
print(l)