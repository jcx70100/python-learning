#encoding = utf-8

# 存储网站和密码
# 实现增删改查功能

# 打印功能菜单
def show_manu():
    print("----密码管理系统 v0.1----")
    print("1.新增密码")
    print("2.删除密码")
    print("3.修改密码")
    print("4.查询密码")
    print("5.打印所有密码")
    print("6.退出")


    # 功能函数
def new_passwd():
    new_addr = input("请输入网址：")
    new_pass = input("请输入对应的密码：")
    passwd = {}
    passwd["address"] = new_addr
    passwd["password"] = new_pass
    passwds.append(passwd)
    print("网址\t密码")
    print("%s\t%s"%(passwd["address"],passwd["password"]))

def del_passwd():
    del_addr = input("请输入要删除的网址：")
    for item in passwds:
        if del_addr == item["address"]:
            passwds.remove(item)
            print("删除成功！")
            break
    else:
        print("无匹配网址！")

def edit_passwd():
    edit_addr = input("请输入要修改的网址：")
    for item in passwds:
        if edit_addr == item["address"]:
            new_addr = input("请输入新的网址：")
            new_pass = input("请输入对应的密码：")
            item["address"] = new_addr
            item["password"] = new_pass
            print("网址\t密码")
            print("%s\t%s"%(item["address"],item["password"]))
            break
    else:
        print("无匹配网址！")

def find_passwd():
    find_addr = input("请输入要查询的网址：")
    for item in passwds:
        if find_addr == item["address"]:
            print("网址\t密码")
            print("%s\t%s"%(item["address"],item["password"]))
            break
    else:
        print("无匹配网址！")

def show_all():
    print("网址\t密码")
    for item in passwds:
        print("%s\t%s"%(item["address"],item["password"]))

def save_pass(passwds):  #保存密码到文件
    f = open("pass.txt","w")
    for item in passwds:
        f.write(str(item)+"--")  # 写入特殊字符串，方便导入的时候进行格式区分
    f.close()


#---------main---------#

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