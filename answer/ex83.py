def fun(n):
    if n == 6174:
        print ('6174')
        return
 
    a = []
    while n:
        a.append(n % 10)
        n //= 10
    a.sort()
 
    s = 0
    k1 = 1
    k2 = 1000
    for x in a:
        s += x * (k1 - k2)
        k1 *= 10
        k2 //= 10
 
    fun(s)
 
fun(1234)