# -*- coding: UTF-8 -*-
if __name__ == '__main__':
    a = input('请输入4位以上数字:\n')
    if a.isdigit() and len(a) >= 4:
        print('输入 %s，\t输出 %s。' %(a,a[4:8]))