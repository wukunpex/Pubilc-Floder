#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 7.4.2 去重
'''
集合去重复有局限性
1，只能争对不可变类型
2，集合本身是无序的，去重之后无法保留原来的顺序
'''
l = ['a', 'b', 1, 'a', 'a']
s = set(l)
print(s)  # 将列表转成了集合
l_new = list(s)  # 再将集合转回列表
print(l_new)
# 争对不可变类型，并且保证顺序则需要我们自己写代码实现，例如

list1 = [
    {'name': 'shiping', 'age': 90, 'sex': 'male'},
    {'name': 'jack', 'age': 22, 'sex': 'male'},
    {'name': 'tom', 'age': 34, 'sex': 'female'},
    {'name': 'shiping', 'age': 90, 'sex': 'male'},
    {'name': 'shiping', 'age': 90, 'sex': 'male'}
]
list2 = []
# print(list1)
for dic in list1:
    if dic not in list2:
        list2.append(dic)
print(type(list2), list2)
# 长度
print(len(list2))
# 2成员运算
print({'name': 'shiping', 'age': 90, 'sex': 'male'} in list2)
# for 循环
for item in list2:
    print(item)

python = {'shiping', 'xunliang', 'wanglei', 'wangfei', 'zhangjuan'}
linux = {'weiyi', 'shiyue', 'wanglei', 'xunliang', 'shiping'}
# 求出即报名python 又报名linux课程的学员名字集合
print('40', python & linux)
# 求出所有报名的学生名字集合
print(python | linux)
# 求出只报名python课程的学员名字
print(python - linux)
# 求出没有同时这两门课程的学员名字集合
print(python ^ linux)
