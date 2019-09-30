def sum(a, k, n):
    s = a
    for i in range(1, n):
        s += a + i * k 
    return s
 
def mul(a, k, n):
    s = a  
    for i in range(1, n):
        s *= a + i * k 
    return s
 
for a in range(1, 28 // 4):
    find = False
    k = 1
    while True: 
        t = sum(a, k, 4)
        if t >= 28: 
            if t == 28 and mul(a, k, 4) == 585:
                find = True
            break
        k += 1
    if find:
        for i in range(4):
            print (a + i * k,end=' ') 