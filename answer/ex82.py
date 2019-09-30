# coding:utf8
def fun(n):
    print(n,end=' ')
    while n != 1:
        n = 3 * n + 1 if n % 2 else n // 2

    print('finished')
 
for i in range(2, 1000):
    fun(i)