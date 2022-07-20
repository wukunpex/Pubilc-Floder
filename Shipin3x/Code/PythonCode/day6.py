#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3.3 如何使用循环结构
# 3.3.1 while 循环语法

# python 中有while 与 for 两种循环机制，其中while 循环称之为条件循环，语法如下
"""
while 条件：
    代码1
    代码2
    代码3
"""
# 用户认证程序的基本逻辑就是接收用户输入用户名与程序中存放的用户名密码进行判断，判断成功则登陆成功，判断失败则输出账号
username = "shiping"
password = 123
count = 0
tag = True
# inp_name=input("please entries username: ")
# inp_passwd=int (input ("please entries your password: "))

"""
if inp_name == username and inp_passwd == password:
    print('logined successful')
else:
    print ('that you input username and password is bad;\nplease entries your username and password again;')
"""
# 案例二
# while + break的使用
'''
while count < 3:
    inp_name = str(input('please input your account: '))
    inp_password = int(input('please inout your passeord: '))
    if inp_name == username and inp_password == password:
        print('logined successful')
        break
    else:
        print('one of them inputs is bad, input again')
        count += 1

'''
# 案例三while 循环嵌套+break
# 如果嵌套while循环嵌套了很多成，要想退出每一层循环则需要在没有一层循环加上一个break
"""
while count < 3:
    inp_name = str(input('please enter your account: '))
    inp_password = int(input('please enter your password: '))
    if inp_name == username and inp_password == password:
        print('login successful')
        while True:
            cmd = input('>>: ')
            if cmd == 'quit':
                break
            print('run <%s>' % cmd)
        break
    else:
        print('the password or account you entered is wrong over %s times: ' % (count))
        count += 1
"""
# 案例四 while循环嵌套+tag的使用
# 针对嵌套多层的while循环，如果我们的目的很明确就是要在某一层直接退出所有层的循环，
# 其实有一个窍门，就让所有while循环的条件都用同一个变量，该变量的初始值为Ture，
# 一旦在某一层将该变量的值改为False，则所有层的循环都结束
"""
while tag:
    inp_name = str(input("please enter your account: "))
    inp_password = int(input("please enter your password: "))
    if inp_name == username and inp_password == password:
        print('logined successful')
        while tag:
            cmd = input('>>: ')
            if cmd == 'quit':
                tag=False
                break
            else:
                print('run %s' %(cmd))
    else:
        print('The password and account you inputs is wrong')
        count += 1
"""
# 案例五 while + continue
# break 代表结束本层循环， 而continue 则用于结束本次循环，直接进入下一次循环
# 打印1到10之间，除7以外的所有数字
number = 11
while number > 1:
    number -= 1
    if number == 7:
        #break
        continue
    else:
        print(number)
