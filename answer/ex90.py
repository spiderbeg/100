#coding:utf-8
 
# 1. 生成 1,3,5,7,9 全排列, 每种排列是一个元组
# 2. 元组转换成数字 (例: 13579,357,159)
# 3. 检测3个数字是素数，如全是素数则是金蝉数
from functools import reduce
import math
def isPrimeNum(n):
    for k in range(2, int(math.sqrt(n) + 1)):
        if n % k == 0: 
            return False
    return True
 
from itertools import permutations
for p in permutations([1,3,5,7,9], 5):
    # (3,5,7), (1,5,9), (1,3,5,7,9) 
    for l in (p[1:-1], p[::2], p):
        s = reduce(lambda x, y: 10 * x + y, l)
        if not isPrimeNum(s): 
            break
    else:
        print(p) 