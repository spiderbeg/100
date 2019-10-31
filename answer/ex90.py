#coding:utf-8
 
# 1. 生成 1,3,5,7,9 全排列, 每种排列是一个元组
# 2. 元组转换成数字 (例: 13579,357,159)
# 3. 检测3个数字是素数，如全是素数则是金蝉数
# 4. 健侧中间的一位数是否为素数，素数大于1.
from functools import reduce
import math
def isPrimeNum(n):
    for k in range(2, int(math.sqrt(n) + 1)):
        if n % k == 0: 
            return False
    return True
 
from itertools import permutations
for p in permutations([1,3,5,7,9], 5): # 五位数的所有组合
    # (3,5,7) (1,3,5,7,9) 5
    for l in (p[1:-1], p): # p[1:-1]：同时去掉最高位与最低位数字后的三位数
        s = reduce(lambda x, y: 10 * x + y, l) 
        if not isPrimeNum(s): 
            break
    else:
        if isPrimeNum(p[2]) and p[2]>1: # p[2]:同时去掉它的最高位与最低位数字后的三位数还是素数，同时去掉它的高二位与低二位数字后的一位数还是素数。对于中间一位数进行判断
            print(p) 