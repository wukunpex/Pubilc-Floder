#!/usr/bin/env python
# -*- coding: utf-8 -*-
# datetime: 2022/9/22 19:41
# software: PyCharm
import shelve
import time
import os

f = shelve.open('bd.shl')
f['stu1'] = {'name': 'shipping', 'age': '29'}
print(f['stu1']['name'], f['stu1']['age'])

f.close()
# time.sleep(10)
os.remove('bd.shl.bak')
os.remove('bd.shl.dat')
os.remove('bd.shl.dir')
