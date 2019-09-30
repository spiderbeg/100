# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    a = input('请输入一段字符\n')
    z = {}
    for i in a:
        z[i]  = z.get(i, 0) + 1
    for i in z:
        print('字符：%s, 出现次数：%s。' %(i, z[i]))