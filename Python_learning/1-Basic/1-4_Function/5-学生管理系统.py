# encoding = utf-8

# 学生信息管理系统
# 实现数据增删改查
# 内容 - 学号，姓名，年龄


cards = []
# 输出功能目录
def show_manu():
    print("="*50)
    print("1.新建学生信息")
    print("2.修改学生信息")
    print("3.查找学生信息")
    print("4.删除学生信息")
    print("5.显示学生信息")
    print("6.退出系统")


# 新建学生信息
def new_card():
    new_name = input("请输入学生姓名：")
    new_age = int(input("请输入学生年龄："))
    new_num = input("请输入学生学号：")
    card = {}  #定义新的字典用于存放学生信息
    card["name"] = new_name
    card["age"] = new_age
    card["number"] = new_num
    cards.append(card)  # 学生信息以字典形式存进cards列表
    print("姓名\t年龄\t学号")   #输出新的学生的信息
    print("%s\t%d\t%s"%(card["name"],card["age"],card["number"]))


# ---------  查找功能区 ----------#
# 查找功能菜单
def find_manu():
    print("请输入查找类型：")
    print("1-按姓名查找")
    print("2-按学号查找")
    find_code = int(input("请输入查找功能编号：")) #获取菜单编号
    return find_code

# 实现查找功能
def find_card():
    find_code = find_manu()  # 获取查询菜单号
    if find_code is 1:   # 按照姓名查询
        find_name = input("请输入要查找的姓名")
        for temp in cards:  # 遍历名片列表
            if find_name in temp["name"]: # 找到要查询的信息
                print("姓名\t年龄\t学号")   # 打印输出要查找的信息
                print("%s\t%d\t%s"%(temp["name"],temp["age"],temp["number"]))
                break
        else:
            print("查无此人！")
    else:  # 按照学号查找
        find_number = input("请输入要查找的学号")
        for temp in cards:
            if find_number in temp["number"]:  # 找到对应学号
                print("姓名\t年龄\t学号")
                print("%s\t%d\t%s"%(temp["name"],temp["age"],temp["number"]))
                break
        else:
            print("查无此人！")


# --------- 编辑学生信息功能块 --------#
def edit_manu():
    print("请输入修改类型：")
    print("1-修改姓名")
    print("2-修改学号")
    print("3-修改年龄")
    code = int(input("请输入功能编号：")) #获取功能编号
    return code

# 实现信息修改
def edit_card():  # 可以统一通过姓名查询来简化程序
    code = edit_manu()  # 获取编辑功能编号
    if code == 1:  # 修改姓名
        find_name = input("请输入要修改的姓名：")
        for temp in cards:
            if find_name in temp["name"]:   # 找到信息库中对应的姓名
                new_name = input("请输入新的姓名：")  # 获取新的姓名
                temp["name"] = new_name    # 修改姓名
                print("姓名\t年龄\t学号")
                print("%s\t%d\t%s"%(temp["name"],temp["age"],temp["number"]))
                break
        else:
            print("查无此人！")
    if code == 2:  # 修改学号
        find_name = input("请输入要修改的学号：")
        for temp in cards:
            if find_name in temp["number"]:
                new_name = input("请输入新的学号：")
                temp["number"] = new_name
                print("姓名\t年龄\t学号")
                print("%s\t%d\t%s"%(temp["name"],temp["age"],temp["number"]))
                break
        else:
            print("查无此人！")
    if code == 3:  # 修改年龄
        find_name = input("请输入要修改的姓名：")
        for temp in cards:
            if find_name in temp["name"]:
                new_name = int(input("请输入新的年龄："))
                temp["age"] = new_name
                print("姓名\t年龄\t学号")
                print("%s\t%d\t%s"%(temp["name"],temp["age"],temp["number"]))
                break
        else:
            print("查无此人！")

# 删除信息
def del_card():
    del_name = input("请输入要删除的学生姓名：")
    for temp in cards:
        if del_name in temp["name"]:  # 找到要删除的学生信息
            cards.remove(temp)  # 删除信息
            print("删除成功！")
            break
        else:
            print("查无此人！")

# 打印所有学生信息
def show_cards():
    print("姓名\t年龄\t学号")
    for temp in cards:
        print("%s\t%d\t%s"%(temp["name"],temp["age"],temp["number"]))


while True:
    show_manu()
    # 获取用户输入
    try:
        num = int(input("请输入功能项编号："))
    except:
        print("您的输入有误，请重新输入！！")
        continue

    # 执行用户指令
    if num == 1:
        new_card()
    elif num == 2:
        edit_card()
    elif num == 3:
        find_card()
    elif num == 4:
        del_card()
    elif num == 5:
        show_cards()
    elif num == 6:
        break
    else:
        print("请输入功能菜单中的对应数字！")

