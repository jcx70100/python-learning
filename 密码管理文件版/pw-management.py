#encoding = utf-8

# 存储网站和密码
# 实现增删改查功能


class pw_management(object):
    def __init__(self):
        self.passwds = [] # 用于存放所有的密码信息
        self.passwd_temp = {}  # 构建单个密码信息
    
    #创建新密码
    def new_passwd(self):
        self.passwd_temp["address"] = input("请输入新的网址：")
        self.passwd_temp["password"] = input("请输入对应的密码：")
        #print(self.passwds)
        self.passwds.append(self.passwd_temp)
        #print(self.passwds)
        self.passwd_temp = {}
        #self.passwd_temp.clear()
        print("新建成功！")
        #print("网址\t密码")
        #print("%s\t%s"%(passwd["address"],passwd["password"]))

    def del_passwd(self,del_addr):
        #del_addr = input("请输入要删除的网址：")
        for item in self.passwds:
            if del_addr == item["address"]:
                self.passwds.remove(item)
                print("删除成功！")
                break
        else:
            print("无匹配网址！")

    def edit_passwd(self,edit_addr):
        #edit_addr = input("请输入要修改的网址：")
        for item in self.passwds:
            if edit_addr == item["address"]:
                #new_addr = input("请输入新的网址：")
                #new_pass = input("请输入对应的密码：")
                item["address"] = input("请输入新的网址：")
                item["password"] = input("请输入对应的密码：")
                #print("网址\t密码")
                #print("%s\t%s"%(item["address"],item["password"]))
                print("修改完成！")
                break
        else:
            print("无匹配网址！")

    def find_passwd(self,find_addr):
        #find_addr = input("请输入要查询的网址：")
        for item in self.passwds:
            if find_addr == item["address"]:
                print("网址\t\t密码")
                print("%s\t%s"%(item["address"],item["password"]))
                break
        else:
            print("无匹配网址！")

    def show_all(self):
        print("网址\t\t密码")
        for item in self.passwds:
            print("%s\t%s"%(item["address"],item["password"]))
    
    #def __str__(self):
    #    print("网址\t密码")
    #    for item in self.passwds:
    #        print("%s\t%s"%(item["address"],item["password"]))
        #return for item in self.passwds "%s\t%s"%(item["address"],item["password"])

    def save_file(self):  #保存密码到文件
        f = open("pass.data","w")
        f.write(str(self.passwds))
        #for item in passwds:
        #    f.write(str(item)+"--")  # 写入特殊字符串，方便导入的时候进行格式区分
        f.close()

    def input_file(self):
        try:
            f = open("pass.data")
            self.passwds = eval(f.read())
            f.close()
        except Exception:
            self.passwds = []



# 打印功能菜单
def show_manu():
    print("==== 密码管理系统 v0.2 ====")
    print(" 1.新增密码")
    print(" 2.删除密码")
    print(" 3.修改密码")
    print(" 4.查询密码")
    print(" 5.打印所有密码")
    print(" 6.退出")
    print("===========================")



#---------main---------#






pm = pw_management()
pm.input_file()

while True:
    show_manu()
    # 获取用户输入
    try:
        num = int(input("请输入功能编号："))
    except:
        print("您的输入有误，请重新输入！")
        continue

    #print(pm.passwds)
    #print(pm.passwd_temp)

    # 执行相关操作
    if num == 1:
        pm.new_passwd()
    elif num == 2:
        del_addr = input("请输入要删除的网址：")
        pm.del_passwd(del_addr)
    elif num == 3:
        edit_addr = input("请输入要修改的网址：")
        pm.edit_passwd(edit_addr)
    elif num == 4:
        find_addr = input("请输入要查询的网址：")
        pm.find_passwd(find_addr)
    elif num == 5:
        pm.show_all()
    elif num == 6:
        #save_flag = input("是否保存？(y/n)")
        #if save_flag == 'y'
        pm.save_file()  #退出之前保存密码文件
        break
    else:
        print("您的输入有误，请重新输入！")




'''
passwds = []
try:  # 导入保存的密码文件
    f = open("pass.txt","r")
    content = f.read().split("--")  # 根据特殊字段--将字符串转换成列表
    content.remove("")
    #print(content)
    for temp in content:   # 对列表中每个元素转换为字典
        temp_dir = eval(temp)    #转换为字典
        passwds.append(temp_dir)
    f.close()
    
    #print(passwds)
except:
    passwds = [] #定义空列表存放密码

show_manu()


while True:
    # 获取用户输入
    try:
        num = int(input("请输入功能编号："))
    except:
        print("您的输入有误，请重新输入！")
        continue

    # 执行相关操作

    if num == 1:
        new_passwd()
    elif num == 2:
        del_passwd()
    elif num == 3:
        edit_passwd()
    elif num == 4:
        find_passwd()
    elif num == 5:
        show_all()
    elif num == 6:
        save_pass(passwds)  #退出之前保存密码文件
        break
    else:
        print("您的输入有误，请重新输入！")


# 保存文件
'''