#coding:utf-8
 
#解题思路：
#    1.用列表存储当前小朋友的糖果数.
#    2.模拟糖果传递过程, (s[i-1] + s[i]) / 2
#    3.判断是否全相等
 
def fun():
    s = [10, 2, 8, 22, 16, 4, 10, 6, 14, 20]
 
    count = 0
    while not all([x == s[0] for x in s]):
        s = [(s[i-1] + s[i]) / 2 for i in range(10)]
        s = [x + x % 2 for x in s]
        count += 1
 
    print (count, s)
 
fun()