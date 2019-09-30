# coding: utf-8

def shape(row=5, col=5, dot='*'):
    # 图形函数，三个默认参数
    # 绘制图形，循环 row 行
    for i in range(row):
        # 每行画 col 次图案
        print(dot * col)

# 函数调用与赋值
shape()
shape(4, 3)
shape(2, 6, dot='!')