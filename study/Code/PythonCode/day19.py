#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 集合
# 7.1 集合，list tuple，dict 一样都可以存放多个值，但是集合主要用于：去重，关系运算
# 定义：在{}内用逗号分隔开多个元素，集合具备以下三个特点
'''
1:每个元素必须是不可变类型
2:集合内没有重复的元素
3:集合内元素无序
'''
set1 = {1, 2, 3, 4}  # set1=set({1,2,3,4})
print(type(set1), set1)
# 注意1：列表类型是索引对应值，字典是key对应值，均可以取得单个指定的值，而集合类型既没有索引也没有key与值对应，所以无法取得单个\
# 的值，而且对于集合来说，主要用于去重与关系元素，根本没有取出单个指定值这种需求。

# 注意2：{}即可以用于定义dict，也可以用于定义集合，但是字典内的元素必须是key：value的格式，现在我们想定义一个空字典和空集合\
# 该如何准确去定义两者

dict1 = {}  # 默认是空字典
set1 = set()  # 这才是定义空集合

# 7.3类型转换
# 但凡能被for循环的遍历的数据类型（强调：遍历出的每一个值都必须为不可变类型）都可以传给set（）转换成集合类型
s = set([1, 2, 3, 4])
s1 = set((1, 2, 3, 4))
s2 = set({'name': 'shiping', })
s3 = set('who')
print(s, s1, s2, s3)

str1 = (1, 2, 3, 4, 5)
str2 = {1, 2, 3, 4, 5}
str3 = [1, 2, 3, 4, 5]
str4 = {'name': '', 'age': ''}
print(type(str1), type(str2), type(str3), type(str4), str1, str2, str3, str4)
# 7.4 运算
# 7.4.1 关系运算
friends1 = {'tianzhou', 'weiyi', 'zhangjuan', 'shiyue'}
friends2 = {'wanglei', 'xunliang', 'zhangjuan', 'shiyue'}
# 合集 （|）：求两个用户所有的好友（重复好友只留一个）
print(friends1 | friends2)

# 2交集（&）：求两个用户的共同好友
print(friends1 & friends2)
# 3差集（-）
print(friends1 - friends2)  # 求用户1独有的好友
print(friends2 - friends1)  # 求用户2独有的好友

# 4，对称差集（^）
print(friends1 ^ friends2)  # 求两个用户独有的好友们（即去掉共同的好友）
# 5， 值是否相等（==）
print(friends1 == friends2)

# 父集 一个集合是否包含另外一个集合
# 6.1 包含则返回true
print({1, 2, 3, } > {1, 2})
print({1, 2, 3, } >= {1, 2})
# 6.2 不存在包含关系，则返回false
print({1, 2, 3} > {1, 3, 4, 5})
print({1, 2, 3} >= {1, 2, 4, 5, 6})
# 7,子集
print({1, 2} < {1, 2, 3})
print({1, 2} <= {1, 2, 3})
