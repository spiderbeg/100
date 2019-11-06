# -*- coding: UTF-8 -*-
if __name__ == '__main__':
    a = input('请输入7及位以上数字:\n')
    if a.isdigit() and len(a) >= 4:
        print('输入 %s，\t输出 %s。' %(a,a[-7:-3]))