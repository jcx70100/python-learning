#encoding = utf-8
# 输出数据范围内所有的素数

prime_number = []

def prime(begin_num=100,end_num=200):
    '''查找一定数值范围内的质数，默认是100-200范围。'''
    while begin_num <= end_num:
        if number(begin_num) is True:   #是质数
            prime_number.append(begin_num) 
        begin_num += 1


def number(num): #判断素数
    '''判断当前输入数值是否为质数，是的话返回True，否则返回False。'''
    i = 2   #排除因数1
    while i <= num:
        if num%i == 0:  #判断是否存在除1和本身以外的因数
            break  #如果当前i是因数，跳出循环
        i += 1  #如果i不是因数，继续增加
    if i == num:    #i等于本身，说明直存在1和本身的因数，是质数
        return True
    else:
        return False



while True:
# 输入数据范围
    try:
        print("输入0，0表示退出。")
        begin_num = int(input("请输入数据范围最小值："))
        end_num = int(input("请输入数据范围最大值："))
    except:
        break
        print("您的输入有误，请重新输入！")

            # 输出范围内的素数
    if begin_num == 0 and end_num == 0:
        break
    
    prime(begin_num,end_num)
    print(prime_number)