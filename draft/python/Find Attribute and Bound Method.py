#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student:
    school = 'old-boy'

    """
    class 定义一个类的名字
    怎么定义对象独有的特征，就是在内的内部需要定一个函数 def __init__(self)
    """

    def __init__(self, name, age, sex):  # __开头和结尾的这一类就是python自带的
        # 在调用类的时候会自动触发执行
        self.Name = name
        self.Age = age
        self.Sex = sex

    def learn(self):
        # def 定义了一个函数的名字，产生一个函数名字
        # 上面(self)是一个位置形参，位置形参的特性是你在掉用这个函数的时候必须给它传值
        print('%s is learning' % self.Name)

    def choose_cource(self):
        print('choose course')

        # 类的内部是可以有其他可执行代码的
        # 类的代码在类的定义阶段就会立刻执行

    print("=======================================running")


stu1 = Student('XiaoMing', 18, 'Female')
stu2 = Student('Jillane', 21, 'Male')
stu3 = Student('Shipping', 29, 'Male')

# stu4=Student()
# print(stu4) #(TypeError: __init__() missing 3 required positional arguments: 'name', 'age', and 'sex')

print(stu1.__dict__)
print(stu1.Name, stu1.Age, stu1.Sex, stu2.Name, stu2.Age, stu2.Sex)

# 总结
# 1，我查找一个对象的属性顺序是: 先找自己的名称空间__dict__, 再找类的名称空间__dict__.
# 2, 类的数据属性是所有对象共享的，所有对象都执行同一个内存地址

print(Student.school, id(Student.school))  # 类的数据属性
print(stu1.school, id(stu1.school))  # ID 是查看内存的ID 值，不是真是的内存的地址。ID 这个函数只是python实现机制来帮你反应出来他在内存当中的位置
print(stu2.school, id(stu2.school))
print(stu3.school, id(stu3.school))

# 3， 访问对象的技能stu* 绑定给对象使用，不同对象就是不同的绑定方法
# 4， 绑定给谁，就应该由谁来调用，谁来调用就会把谁当做第一个参数传给对应的函数

print(Student.learn)  # 类去访问
print(stu1.learn)  # 函数去访问
print(stu2.learn)  # 函数去访问
print(stu3.learn)  # 函数去访问

stu1.learn()
stu2.learn()
stu3.learn()
