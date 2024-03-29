# designed by cxjiang

# 名片管理系统v0.1
# 1. 显示功能列表
print("="*50)
print("名片管理系统 v0.1")
print("1.添加名片")
print("2.修改名片")
print("3.查询名片")
print("4.删除名片")
print("5.退出系统")
print("6.显示数据库")
print("="*50)


cards = []

while True:
    # 2. 获取用户输入
    num = int(input("请输入您需要的功能："))


    # 3. 执行用户的输入
    if num == 1: #添加名片
        new_name = input("请输入新名片的姓名：")
        new_qq = input("请输入新的qq：")
        new_addr = input("请输入新的住址：")
        new_card = {}  #新建字典，用于存储用户信息
        new_card['name'] = new_name
        new_card['qq'] = new_qq
        new_card['addr'] = new_addr
        cards.append(new_card)
        print("姓名\tqq\t地址")
        print("%s\t%s\t%s"%(new_card['name'],new_card['qq'],new_card['addr']))

    elif num == 2: #修改名片
        old_name = input("请输入要修改的名片姓名：")
        for temp in cards:
            if old_name in temp['name']:
                new_name = input("请输入新的名字：")
                temp['name'] = new_name
                print("修改完成！")
                print("姓名\tqq\t地址")
                print("%s\t%s\t%s"%(temp['name'],temp['qq'],temp['addr']))
                break
        else:
            print("该姓名不在数据库中，请重新查询！！")

    elif num == 3: #查询名片
        find_name = input("请输入要查询的姓名：")
        for temp in cards:
            if find_name in temp['name']:
                print("姓名\tqq\t地址")
                print("%s\t%s\t%s"%(temp['name'],temp['qq'],temp['addr']))
                break
        else:
            print("查无此人！！")
    elif num == 5: #退出程序
        break
    elif num == 4: #删除名片
        delete_name = input("请输入要删除的姓名：")
        for temp in cards:
            if delete_name in temp['name']:
                cards.remove(temp)
                print("删除成功！")
                break
        else:
            print("该用户不在数据库中！！")
    elif num == 6:
        print("姓名\tqq\t地址")
        for temp in cards:
            print("%s\t%s\t%s"%(temp['name'],temp['qq'],temp['addr']))
    else:
        print("您的输入有误，请重新输入！！")
