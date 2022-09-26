#!/usr/bin/env python
# -*- coding: utf-8 -*-
# datetime: 9/19/2022 11:02 AM
# Software: PyCharm

import subprocess
import time

# subprocess.Popen('tasklist',shell=True) #subprocess 子进程模块，向操作系统发送一个信号
# print('--------主')
# time.sleep(1)

# For example 1 一个正确的命名执行"tasklist"
obj = subprocess.Popen('tasklist', shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,

                       )  # 结果丢到管道里去了
print('1st time read value', obj.stdout.read().decode('gbk'))  # 在正确的管道取值打印, Win 用decode('gbk')解码，Linux用UTF-8
print('2nd time read value ', obj.stdout.read().decode('gbk'))  # 在正确的管道取值打印,当第一次取值后，第二次就没有值可取了。
# decode.(gbk)编码后编程Unicode的格式
print('FOR Example 1st------major')
time.sleep(1)

# For example 2 输入一个错误的命令去执行"dddddtasklist"

obj1 = subprocess.Popen('ddddtasklist', shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,

                        )  # 结果丢到管道里去了
print('For Example 2nd', obj.stdout.read())
print('For Example 2nd', obj.stderr.read().decode('gbk'))

# For example 3 了解
# import subprocess #tasklist | findstr python

obj1 = subprocess.Popen('tasklist | findstr python', shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )

print('For Example 3rd', obj1.stdout.read().decode('gbk'))

# For Example 4th,一个程序的输出作为另一个程序的输入
obj2 = subprocess.Popen('tasklist', shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )

obj3 = subprocess.Popen('findstr cmd', shell=True,
                        stdin=obj2.stdout,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )

print('For Example 4th', obj3.stdout.read().decode('gbk'))
