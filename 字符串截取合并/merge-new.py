# encoding = utf-8
# created by Jerry Cheng

# 实现多数组内容提取合并
# 内容提取后删除原数组对应的内容
# 如果数组内容不够，或者是空数组，则提取剩余全部内容

# -------------通过面向对象的方法实现 ------------#
# 将导入的数组信息、合并的字符串、截取长度作为类的属性

class str_merge():

    def __init__(self):
        self.data = []
        self.merge_data = ""
        self.length = 0
    
    def __str__(self):
        #打印输出
        return "提取的新数组为： %s"%(self.merge_data)
        
    # 打印功能
    def show_menu(self): 
        print("-"*50)
        print("该程序从文件获取数组信息，按用户需求提取指定长度的信息进行合并。")
        print("-"*50)
    
    # 从文件获取数组信息
    def get_file(self):
        '''该函数实现根据用户输入的文件名来获取文件中的数组信息，每行识别为一个数组。'''
        file_name = input("请输入数组文件名(包含后缀)：")
        f = open(file_name,"r")  # 读取文件
        contents = f.readlines()  # 将文件内容按行存储到contents中
        #print(contents)
        for item in contents:  # 处理文件内的数组数据
            item = item.split()  # 删除文件中导入的每行数据最后的换行符
            self.data = self.data + item   # 将数组数据存入data列表，每个数组为data列表中的一个元素
        print("原始数组信息为：%s"%(str(self.data)))

    # 获取要截取的数据长度
    def get_length(self):
        self.length = int(input("请输入数据段长度："))
    
    #  数组提取与合并,并删除每个数组中已提取的内容
    def merge(self):
        for item in self.data:
            #get_string(item,self.length)
            self.merge_data += item[0:self.length]
            self.data[self.data.index(item)] = item[self.length:]
        print("提取后数组信息： %s"%(str(self.data)))
        #print("提取的新数组为：%s"%(self.merge_data))


#--------------主程序--------------#

zhuzhu = str_merge() #定义一个叫猪猪的对象

zhuzhu.show_menu() # 显示功能
zhuzhu.get_file()  # 从文件获取数组信息
zhuzhu.get_length()  # 获取用户需要截取的长度
zhuzhu.merge()   # 合并截取的字符串并将已截取部分从原字符串删除

print(zhuzhu)  # 打印结果



