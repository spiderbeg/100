# encoding:utf8
tmp = 0
for num in range(1,101):
    # 质数大于 1
    if num > 1:
        # 查看因子
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"不是质数")
                break
        else:
            tmp+=num
            print(num,"是质数")
    # 如果输入的数字小于或等于 1，不是质数
    else:
        print(num,"不是质数")
print('1-100内质数之和 %s .'%tmp)