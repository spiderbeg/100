# -*- coding: UTF-8 -*-
 
if __name__ == '__main__':
    a = [1,4,6,9,13,16,19,28,40,100]
    print ('原始列表: %s' %a)
    number = int(input("\n插入一个数字:\n"))
    lena = len(a)
    for i in range(lena):
        if a[0] > number:
            a.insert(0,number)
            break
        elif a[lena-1]<number:
            a.append(number)
            break
        elif i not in [0,lena-1]:
            if a[i]<= number <=a[i+1]:
                a.insert(i,number)
                break

    print ('排序后列表: %s .'%a)