#!/usr/bin/env python
# -*- coding: utf-8 -*-
# datetime: 9/23/2022 9:07 AM
# Software: PyCharm

import os
import pickle
import json

# json 序列化
# 把内存里边的数据结构保存下来 ， 字典，列表，元组，字符串
# 存在内存里边的特点是什么？ 断电丢失数据
dic = {'a': 1, 'b': 23}  # 只要程序不结束，会一直保存在内存。 断电就没有了
# 如果你想永久保存下来，涉及到一个问题保存到数据库或文件

# 保存到文件里，怎么写
print(str(dic))  # 转成字符串类型

# 目的，保存内存中的数据
# 序列化就是把内存的数据用某种方式保存到硬盘上，保存的目的是为了再次启动程序重新加载到内存里面

# 方法一
with open('db.txt', 'w', encoding='utf-8') as f:
    f.write(str(dic))

# time.sleep(2)
# 重新加载到内存
with open('db.txt', 'r', encoding='utf-8') as f:
    # dic = eval(f.read())  # 转换成原来的字典结构,用eval,其功能是把表达式拿出来的得到一个值
    dic = eval(f.read())
    print(dic['b'])  # eval 根本不是干序列化的事，它只是单独拿出了值; Json he pickle 才是干序列化的事

dic1 = {'d': 29}
x = None
res1 = json.dumps(dic1)
res2 = str(dic1)

print('learning json', res1, type(res1))  # learning json {"d": 29} <class 'str'> #json 格式都用双引号"d"
print('learning json', res2, type(res2))  # learning json {'d': 29} <class 'str'>
print(type(json.dumps(x)), json.dumps(x))

user = {'name': 'Shipping', 'age': 18, 'nb': True}
with open('user.json', 'w', encoding='utf-8') as f1:
    f1.write(json.dumps(user))

# 上面方法过于复杂，用一种简单方法写，如下。一步到位
json.dump(user, open('user-new.json', 'w', encoding='utf-8'))

# 为什么要序列化: 要把内存的数据保存在硬盘。序列化可以跨平台交换数据。

# pickle 序列化

s = {1, 2, 3, 4}  # 定义集合
print(pickle.dumps(s))  # pickle 是一个bytes 类型
# print(json.dumps(s))  # 尝试用json 去序列化会报错;TypeError: Object of type set is not JSON serializable
'''
pickle 序列化的结果与json 序列化的结果的区别
1，json 是一个单纯的 字符串 类型
2，pickle 是一个bytes类型
既然是bytes类型，我要往文件里写文件就的用bytes打开

'''
# pickle 序列化
# 第一种方式写
# with open('s.pkl', 'wb') as f:
#     f.write(pickle.dumps(s))

# 第二种方式写
pickle.dump(s, open('s.pkl', 'wb'))

# pickle 反序列化

# 第一种方式写
# with open('s.pkl', 'rb') as f:
#     s = pickle.loads(f.read())
#     print(s, type(s))

# 第二种方式写
s = pickle.load(open('s.pkl', 'rb'))
print(s, type(s))

# 删除生成的文件s.pkl
os.remove('s.pkl')
