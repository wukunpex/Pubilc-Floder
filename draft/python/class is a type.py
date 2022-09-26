#!/usr/bin/env python
# -*- coding: utf-8 -*-
# datetime: 2022/9/18 15:14
# software: PyCharm

# 类即是类型
l1 = [1, 2, 3, 4]  # l=list([1,2,3,4])


class Teacher:
    school = 'old-boy'  # 也有相似的属性
    # 方便t1,t1,t3都能访问到次数，需要把这个属性变成类的数据属性
    count = 0  # 初始化count=0

    def __init__(self, name, sex, age, level, salary):  # 定义老师独有特征，年龄，性别
        # "__init__" 的意思是什么阶段就为对象添加自己独有的特征？
        # * 是在初始化阶段，是在第一次实例化的时候就为对象定义了自己独有的特征了，这是这个函数的意义所在 *

        self.name = name
        self.sex = sex
        self.age = age
        self.level = level
        self.salary = salary

        Teacher.count += 1  # 处理的时候用Teacher去处理，就能反应给所有的对象

    # 教学技能
    def teach(self):
        print('%s is teaching' % self.name)


t1 = Teacher('Shipping', 'male', 23, 1, 200000)
l2 = [1, 2, 3, 4]  # l=list([1,2,3,4])

print(type(t1))
print(type(l1), id(l1))
print(type(l2), id(l2))
print(t1.__dict__)
print(t1.name, t1.salary)

print(l1.append)
list.append(l1, 19)
print(type(l1))
