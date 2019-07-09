#encoding = utf-8

#计算当前是今年的第几天


def date_number(date):
    num = 0
    leap_date = (31,28,31,30,31,30,31,31,30,31,30,31) #闰年每月天数
    
    for item in leap_date[0:int(date[4:6])-1]: #计算当月之前的天数
        num += item
    num += int(date[6:]) #加上当月天数
    if leap_year(int(date[0:4])) is True: #是闰年
        return num
    elif int(date[4:6]) > 2: # 不是闰年，且月份大于2，总天数+2（平年天数）
        return num+2
    else:   # 不是闰年，但是属于1月份
         return num
    

def leap_year(num): #判断闰年
    if num%400 == 0 or (num%4 ==0 and num%100 != 0):  #判断是否是闰年
        return True   # 是闰年，返回True
    else:
        return False

# 获取用户输入当前日期
today = input("请输入当前日期，格式为20190101(输入00退出):")
# 计算天数

# 输出天数
dates = date_number(today)
print("今天是今年的第%d天"%dates)