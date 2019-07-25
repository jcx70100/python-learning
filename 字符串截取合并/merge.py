# encoding = utf-8
# created by Jerry Cheng

# 实现多数组内容提取合并
# 内容提取后删除原数组对应的内容
# 如果数组内容不够，或者是空数组，则提取剩余全部内容

#-------------定义全局变量------------#
merge_data = "" #存储合并后的数据
data = []  # 用于存放文件中的数组信息，每个数组为列表中的一个元素

#-------------定义子函数-------------#
# 打印功能
def show_menu(): 
    print("-"*50)
    print("该程序从文件获取数组信息，按用户需求提取指定长度的信息进行合并。")

# 从文件获取数组信息
def get_file():
    '''该函数实现根据用户输入的文件名来获取文件中的数组信息，每行识别为一个数组。'''
    file_name = input("请输入数组文件名(包含后缀)：")
    global data  # 对全局变量进行操作
    f = open(file_name,"r")  # 读取文件
    contents = f.readlines()  # 将文件内容按行存储到contents中
    #print(contents)
    for item in contents:  # 处理文件内的数组数据
        item = item.split()  # 删除文件中导入的每行数据最后的换行符
        data = data + item   # 将数组数据存入data列表，每个数组为data列表中的一个元素
    print("原始数组信息为：%s"%(str(data)))

# 数组提取与合并
def get_string(data,length):
    '''该子函数实现对单个数组进行截取，截取length长度的字符串，并将提取部分合并为新字符串。'''
    global merge_data # 对全局变量进行操作
    merge_data += data[0:length]

#  删除每个数组中已提取的内容
def merge(data,length=0):
    for item in data:
        get_string(item,length)
        data[data.index(item)] = item[length:]

#------------------主程序------------------#

show_menu()

get_file()

# 获取要截取的数据长度
length = int(input("请输入数据段长度："))

merge(data,length)

#打印输出
print("提取的新数组为：%s"%(merge_data))
print("提取后的数组信息如下：\n %s"%(str(data)))