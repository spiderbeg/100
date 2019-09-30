# 获取用户输入数字
lower = 1
upper = 10000
 
for num in range(lower,upper + 1):
   # 初始化 sum
   sum = 0
   # 指数
   n = len(str(num))
   # 检测
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** n
       temp //= 10
 
   if num == sum:
       print(num)