# encoding:utf8
# 假设输入正确的情况
for i in range(7):
    a = int(input('input a number:\n'))
    while a < 1 or a > 50:
        a = int(input('input a number:\n'))
    print(a * '*')