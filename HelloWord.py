list=[1,2,"hello",4]
print(list)
list1=[]
list1.append(666)
list1.append(777)
list1.append(444)
del list1[0]

print("长度是=",len(list1))

print("list1 * 4 =",list1*4)

print("444 是否在 list1 内呢？=",444 in list1)

for i in list1:
    print("list1 元素遍历：",i)


print("list1中倒数第二个",list1[-2])

print("list1 最大的元素=",max(list1))

print("------------------------元组--------------------------")
tup1=("physics","chemistry",1997,2000)
print("输出元组=",tup1)
tup2=(1, 2, 3, 4, 5 )
print("元组第一个元素：",tup1[0])

for  n in tup1:
    print("元组遍历",n)

print("------------------------字典是大括号并且是以：连接的key value 值--------------------------")
# 创建一个字典
dic={"a":1,"b":2,"c":3}
# 获取某个元素
print(dic["c"])
# 增加一个元素
dic["d"]=4
print("增一个键值对之后",)
print(dic)
# 对字典清空
dic.clear()
print(dic)

print("------------------------import time--------------------------")
import time

print(time.localtime())
print("格式化后",time.strftime("%Y %m %d %H %M %S",time.localtime()))






