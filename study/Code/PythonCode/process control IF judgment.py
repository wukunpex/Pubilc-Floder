# !/usr/bin/env python
# -*- coding: utf-8 -*-
age = int(input(">>:"))
is_pretty = True
height = 170
weight = 80
# if True:
if (age > 18 and age < 22) or is_pretty==True:
    print('to clearing him')
else:
    print('hello aunt')

f = open("day20.py",'rt',encoding='utf-8')
line = f.read()
print(line)
f.close()
