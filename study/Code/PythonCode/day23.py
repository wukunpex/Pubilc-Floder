#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3,1,案例一：r模式的使用
with open('day20.py', mode='r', encoding='utf-8') as f:
    res = f.read()  # 会将文件的内容由硬件全部读入内存，赋值给res

# 小练习：实现用户认证功能
inp_name = input('please enter your name: ').strip()
inp_pwd = input('please enter user passwd: ').strip()
with open(r'C:\Users\shipin3x\OneDrive - Intel Corporation\Desktop\a1.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        # 把用户输入的名字与密码与读出内容做比对
        u,p = line.strip('\n').split(':')
        print(u,p)
        if inp_name == u and inp_pwd == p:
            print('Recognition successfully')
            break
        else:
            print('Incorrect account name or password')
