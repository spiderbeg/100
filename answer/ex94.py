import math
def isPrimeNumber(num):
    i = 2
    x = math.sqrt(num)
    while i < x:
        if num%i == 0:
            return False
        i += 1
    return True
 
def masonNumber(num):
    arr = []
    for i in range(2, num + 1):
        if isPrimeNumber(i) and isPrimeNumber(2**i - 1):
            arr.append(2**i - 1)
    return arr
 
print (masonNumber(50))