#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 八可变类型与不可变类型
# 可变数据类型：值发生改变时，内存地址不变，即ID 不变，证明在改变原值
# 不可变类型：值发生改变时，内存地址也发生改变，即ID 改变，证明是没有在改变原值，是产生了新的值
print('数字类型')
digital = 10
print(id(digital))
digital = 20
print(id(digital), '\n内存地址改变了，说明整形是不可变数据类型，浮点型也一样')

print('2,字符串')
str1 = 'shiping'
print(id(str1))
str1 = 'weiyi'
print(id(str1), '\n内存地址改变了。说明字符串是不可变数据类型')

print('#列表')
list1 = ['shiping', 'weiyi', 'jack']
print(id(list1), list1)
list1[2] = 'xiaowang'
print(id(list1), list1)
list1.append('xiaohua')
print(id(list1), list1, '\n#对列表的值进行操作时，值改变但内存地址不变，所以列表是不可变数据类型')

print('元组')
tuple1 = ('tom', 'jack', [1, 2, 3, 4, 5])
print(tuple1, "\ntuple1[0]='TOM' #报错Typeerror\ntuple.append('lili')# 报错：typeerro")
# 元组内的元素无法修改，指的是元组内索引指向的内存地址不能被修改
print(id(tuple1[0]), id(tuple1[1]), id(tuple1[2]))
tuple1[2][0] = 'bing'
print(tuple1)
print(id(tuple1[0]), id(tuple1[1]), id(tuple1[2]), '\n如果元组中存在可变类型,是可以修改,但是修改后的内存地址不变,查看ID任然不变')
print('字典')
dic = {'name': 'shiping', 'sex': 'female', 'age': '18'}
print(id(dic))
dic['age'] = 19
print(id(dic), '\n对字典进行操作时，值改变的情况下，字典的ID 也是不变，即字典也是可变数据类型')
import os

print(os.getcwd())
