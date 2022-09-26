#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1. get()
dic = {'k1': 'jason', 'k2': 'tony', 'k3': 'chaoyou'}
# ps 字典取值建议使用get()方法
print(dic.get('k2'))  # key 存在，则获取key对应的value值
print(dic.get('kk'))  # key 不存在，不会报错而是默认返回None
print('7', dic.get('kg', 'there is not value'))  # key 不存在时，可以设置默认返回的值

# 2.pop
print(dic)
print('12',dic.pop('k2'))  # 删除指定的key对应的键值对，并返回值
print(dic)

# 3.popitem
dic1 = {'name': 'ping', 'age': 18, 'role': 'testor', 'sex': 'male'}
print(dic1)
print('18',dic1.popitem())
print(dic1)

# 4 update()
# 用新字典更新旧字典，有则修改，无则添加
dic2 = {'k4': '1', 'k5': '2', 'k6': '3', 'k7': '4'}
print('24',dic2)
dic2.update({'k5': '55', 'k8': 'hello', 'k9': 'Hi'})
print(type(dic2),dic2)

# fromkeys()
dic3=dic2.fromkeys(('k5','k4'),'hello')
print(type(dic3),dic3)
print(dic3.get('k4'))

#6 setdefault()
#key 不存在则新增了键值，并将新增的value返回
dic4={'k1':111,'k2':222}
dic5=dic4.setdefault('k3',333)
print(type(dic5),dic5)