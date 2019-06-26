#姓名管理系统 v0.1
#1.功能菜单
print("="*50)
print("1.添加一个姓名")
print("2.修改一个姓名")
print("3.删除一个姓名")
print("4.查找一个姓名")
print("5.exit")
print("="*50)

names = []

while True:
    #2.数据输入
    num = int(input("请输入您需要的功能编号："))
    #if int(num):
    #    num = int(num)
    #else:
    #    print("输入有误，请重新输入！")
    #    continue

    #3.信息处理
    if num == 1:
        add_name = input("请输入要添加的姓名：")
        if add_name in names:
            print("当前用户已存在！")
        else:
            names.append(add_name)
            print("添加成功！！")
            print(names)
    elif num == 2:
        old_name = input("请输入要修改的名字：")
        if old_name in names:
            new_name = input("请输入新的名字：")
            names[names.index(old_name)] = new_name
            print("修改成功！")
            print(names)
        else:
            print("数据库中无此人！")
    elif num == 3:
        del_name = input("请输入要删除的姓名：")
        if del_name in names:
            names.remove(del_name)
            print("删除成功！")
            print(names)
        else:
            print("数据库中无此人！")
    elif num == 5:
        break   
    elif num == 4:
        find_name = input("请输入要查找的姓名：")
        if find_name in names:
            print("找到了！！！")
        else:
            print("查无此人！！")
    else:
        print("您输入的数字不在功能列表中，请重新输入！")

