#encoding = utf-8

# 文件复制

old_file_name = input("请输入要复制的文件名：")
# 打开已知文件文件
old_file = open(old_file_name,"r")
# 新建文件

position = old_file_name.rfind(".")
new_file_name = old_file_name[:position] + "[复件]" + old_file_name[position:]

new_file = open(new_file_name,"w")

while True:
    # 获取就文件内容
    content = old_file.read(1024) #分块拷贝，防止大文件引起的内存错误
    # 写入新文件内容
    if len(content) == 0:
        break
    new_file.write(content)

#关闭新文件
new_file.close()
#关闭就文件
old_file.close()