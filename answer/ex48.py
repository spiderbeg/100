# coding:utf8
 
# 定义一个函数
def mcd(x, y):
   """该函数返回两个数的最大公约数"""
 
   # 获取最小值
   if x > y:
       smaller = y
   else:
       smaller = x
 
   for i in range(1,smaller + 1):
       if((x % i == 0) and (y % i == 0)):
           mc = i
 
   return mc
 
 
# 用户输入两个数字
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
 
print( num1,"和", num2,"的最大公约数为", mcd(num1, num2))