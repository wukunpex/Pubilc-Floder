#!/usr/bin/env python
# -*- coding: utf-8 -*-
str = 'hello shiping'
# 1,按索引取值（正向取，反向取）：
# 1.1 正向取（从左往右）
print(str[9])

username = 'shiping'
passwd = '123'
#inp_name = input ('please inter your account name: ')
#inp_passwd = input ('please inter account password: ')
count = 0
while count < 3:
    inp_name = input ('please inter your account name: ')
    inp_passwd = input ('please inter account password: ')
    if inp_name == username and inp_passwd == passwd:
        print ('login success !')
        while True:
            cmd = input ('>>:')
            if cmd == 'quit':
                break
            print('run <%s>' % cmd)
        break
    else:
        print ('password and account inter error')
        count += 1

import os
print (os.getcwd())