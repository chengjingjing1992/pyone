#获取文件对象

file=open("hello.txt","w")
# strmess="""Python是非常好的 语言！
# 我们都很喜欢她
# """
print("文件名字：",file.name)
file.write("123")
file.write('\n')
file.write("456")
# 关闭打开的文件
file.close()
file1=open("hello.txt");



strreadline=file1.readline()
print("strreadline=",strreadline)

file1.close