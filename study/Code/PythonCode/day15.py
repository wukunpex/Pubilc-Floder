#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 8.2 了解知识; 我们常用的数字类型比较大小，但其实，字符串，列表登都可以比较大小，原理相同：都是一次比较对应位置元素
# 的大小，如果分出大小，则无需比较下一个元素，比如
l1 = [1, 2, 3]
l2 = [1, 2, ]
print(l1 > l2)
# 字符之间的大小取决于他们在ASCII表中的先后顺序，越往后越大
l3 = 'gdsdfasda'
l4 = 'hsfsasadad'
print(l3 < l4)

# 所以我们还可以对下面这个列表排序
l5 = ['a', 'ers', 'goo', 'kk', 'kl', 'jff']
l5.sort()
print(l5)
# 9 循环遍历l5列表里面的值
for i in l5:
    print(i)

list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1[0:6:2])  # 正向步长
print(list1[6::-2])  # 反向步长
