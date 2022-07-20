#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 按key 存取值；可存可取
# 1.1 取
dic = {
    'name': 'shiping',
    'age': 18,
    'hobbies': ['play game', 'basktball'],
}
print(type(dic), dic['name'])
print(dic['hobbies'][1])
# 长度len
print(len(dic))
print('name7' in (dic))
if 'name' in dic:
    print(dic, type(dic), )

print(dic.pop('name'), dic)
dic = {'age': 18, 'hobbies': ['play game', 'basktball'], 'name': 'chengshiping'}
# 获取字典所有的key
print(dic.keys())
# 获取字典所有的value
print(dic.values())
# 获取字典所有的键值对
print(dic.items())
contries = (1, 2, 3, 4, 4, 5, 6)
contries1=tuple('asdfasgagagf')
print(type(contries), contries,contries1,type(contries1))
#循环
#6.1 默认遍历的是字典的key
for key in contries1:
    print(key)

#6.2 只遍历key
for key in dic.keys():
    print(key)
#只遍历value
for key in dic.values():
    print(key)

#遍历key与value
for key in dic.items():
    print(key)