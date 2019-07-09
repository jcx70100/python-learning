#encoding = utf-8

# 判断是否是闰年

def leap_year(num):
    if num%400 == 0 or (num%4 ==0 and num%100 != 0):  #判断是否是闰年
        return True   # 是闰年，返回True
    else:
        return False


while True:
    # 获取用户输入
    try:
        num = int(input("请输入年份(0000表示退出)："))
    except:
        print("您的输入有误，请重新输入！")
        continue
    
    # 输出判断结果
    if num is 0000:
        break
    if leap_year(num) is True:
        print("%d是闰年"%num)
    else:
        print("%d不是闰年"%num)