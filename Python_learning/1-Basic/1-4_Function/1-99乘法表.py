#encode = utf-8

def list(num):
    i = 1
    while i <= num:
        j = 1
        while j <= i:
            print("%d*%d=%d\t"%(j,i,i*j),end="") #最后不换行！
            j += 1
        i +=1
        print("")  #换行


while True:
    try:
        num = int(input("请输入乘法表的最大数值(0表示退出):"))
    except:
        print("您的输入有误，请重新输入！")
        continue
    if num == 0:
        break

    list(num)