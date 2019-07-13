# encoding = utf-8

# 打印文件中除了#开头的内容

# 输入要打开的文件
file_name = input("请输入要打开的文件名：")
# 获取文件内容
f = open(file_name,"r")


contents = f.readlines()
print(contents)

# 打印输出
for temp in contents:
    if temp.startswith("#"):
        #print(end="")
        continue
    else:
        print(temp)

f.close()