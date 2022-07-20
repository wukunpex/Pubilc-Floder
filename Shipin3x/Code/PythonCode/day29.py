#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
如果你已经了解的面向对象编程，就知道类都有一个构造函数，python的构造函数为_init_(),它会再对象初始化的时候执行。
_iter_()方法返回一个特殊的迭代器对象，这个迭代器对象实现了_next_()方法并通过stop iteration异常标识迭代的完成。
_next_()方法（python2里是next()）会返回下一个迭代器对象。
创建一个返回数字的迭代器，初始值为1，逐步递增1；
"""


class mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = mynumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# stop interation 异常用于标识迭代的完成，防止出现无线循环的情况，再__next__（）方法中\
# 我们可以设置在完成指定循环次数后触发stopiteration异常来结束迭代
# 在20次迭代后停止执行
class mynames:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <=20:
            x =self.a
            self.a +=1
            return x
        else:
            raise StopIteration
myclass = mynames()
myiter= iter(myclass)
for x in myiter:
    print(x)
