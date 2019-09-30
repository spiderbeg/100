#coding:utf-8
 
#解题思路：
#   1.令末位数t = 6, 除末位以外部分n
#   2.t连续×10移动到最高位, 再加上n
#   3.t + n == 10 * n + 6 ?
 
# 1236 => 6123 == 4 * 1236
 
def fun(n):
    nn = n
    t = 6
    while nn > 0:
        t *= 10
        nn //= 10
 
    m = 10 * n + 6
    if t + n == m * 4:
        print(m)
 
for x in range(1, 100000):
    fun(x)