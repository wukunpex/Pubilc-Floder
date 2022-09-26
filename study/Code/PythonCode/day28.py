#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 字符串，列表或元组对象都可以用于创建迭代器
list = [1, 2, 3, 4]
it = iter(list)
# print(next(it))
# print(next(it))
for x in it:
    print(x, end="\t")

# 也可以使用next()函数
import sys

list1 = [1, 2, 3, 4, 5]
it1 = iter(list1)
while True:
    try:
        print(next(it1))
    except StopIteration:
        sys.exit()
