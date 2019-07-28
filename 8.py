#coding=utf-8
# 输出 9*9 乘法口诀表。

for i in range(1,10):

    for j in range(1,10):
        a="   "
        if(j<=i):
            print(j, "*", i,"=",i*j ,a,end="")

    print("\n")





















for i  in range(1,10):

    for j in range(1,10):

        if j<=i:
            print(i,"*",j,"=",i*j," ",end="")

    print("\n")
















