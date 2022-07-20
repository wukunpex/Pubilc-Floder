#!/usr/bin/env python
# -*- coding: utf-8 -*-
# list=[1,2,3,4,5,'shiping','rujun',19]
# l=list.__iter__() #等同于l=iter(list)
#
# while True:
#     try:
#         print(l.__next__())#print(next(l))
#     except StopIteration:
#         break
#
# print('=>>>')
#1,总结迭代器有什么优点，不依赖于索引的取值方式，为for循环的实现提供了依据
#2,
# for i in list:
#     print(i)
#
# l=(1,2,3,4,5,6,7,8)
# l_iter=l.__iter__()
# print(l_iter)
# print(next(l_iter))
# print(l.__len__())
#什么是生成器：是要在函数体内部出现yield关键字，那么再执行函数就不会执行函数代码
#会得到一个结果，该结果就是生成器

# def func():
#     print('========1')
#     yield 1
#     print('========2')
#     yield 2
#     print('========3')
#     yield 3
# g=func()
# #生成器就是迭代器
#
# #next(g)
# res1=next(g)
# print(res1)
# res2=next(g)
# print(res2)
#
# #yield 给我们提供了一种自定义迭代器对象的方法
# #yield与return的区别，1 yield可以返回多次值#2，函数暂停与再继续的状态由yield帮忙保存的
# obj=range(1,111111111111,2)
# obj_iter=obj.__iter__()
# print(obj_iter.__next__())
# print(obj_iter.__next__())
# print(obj_iter.__next__())
# print(obj_iter.__next__())
# print(obj_iter.__next__())
def my_range(start,stop,step=1):
    while start < stop:
        yield start #start=1
        start+=step #start +=3
g1=my_range(1,5,2)
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
for i in my_range(1,100,4):
    print(i)
print(g1)
