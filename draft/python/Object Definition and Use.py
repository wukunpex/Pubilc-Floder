#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1，面向过程与面向对象
面向过程：
核心是过程二字，过程即解决问题的步骤，就是先干什么再干什么。基于该思想写程序好比再设计一条流水线，是一种机械方式的思维方式
优点：复杂的过程流程化，进而简单化
缺点：扩展性差

面向对象：
核心是对象二字，对象指特征与技能的结合体
基于该项思想编写程序就好比再创造一个世界，世界是由一个个对象组成，是一种"上帝式"的思想方式
优点：扩展性强
缺点：编程复杂度高，容易出现过度设计

2，类
对象是特征与技能的结合体，类就是一系列对象相似的特征与技能的结合体
在现实世界中：一定是现有的一个个具体存在的对象，后总结出的类
在程序中：一定保证先定义类，后产生对象

3，站在老男孩学校的角度
对象1：
    特征
        学校=老男孩
        名字=世平
        性别=男
        年龄=18
    技能
        吃饭
        睡觉
        玩游戏
对象2：
    特征
        学校=老男孩
        名字=张三
        性别=女
        年龄=38
    技能
        学习
        吃饭
        睡觉

"""


# 在程序中怎么把 [特征] 表示出来: "变量"
# 在程序中怎么把 [技能] 表示出来:"函数"


class Student:
    """
    class 定义一个类的名字
    怎么定义对象独有的特征，就是在内的内部需要定一个函数 def __init__(self)
    """

    def __init__(self, name, age, sex):  # __开头和结尾的这一类就是python自带的
        # 在调用类的时候会自动触发执行
        self.Name = name
        self.Age = age
        self.Sex = sex

    school = 'oldboy'

    def learn(self):
        # def 定义了一个函数的名字，产生一个函数名字
        # 上面(self)是一个位置形参，位置形参的特性是你在掉用这个函数的时候必须给它传值
        print('is learning')

    def choose_cource(self):
        print('choose cource')

        # 类的内部是可以有其他可执行代码的
        # 类的代码在类的定义阶段就会立刻执行

    print("=======================================running")


# print(Student)
print(Student.__dict__)  # 查看类的名称空间

# 查看

# 要访问一个名称空间里的名字有专门的语法 "."
print(Student.school)  # " 数据属性 " 要访问Student 下边的school的属性
# "." 的意思就是访问名称空间的一个名字或名字
print(Student.learn)  # "函数属性"

# 增加

Student.country = "china"  # 加一个属性
print(Student.__dict__)  # 验证该属性是否添加成功，在名称空间查看
print(Student.country)

# 修改
Student.school = 'Oldboy'
print(Student.school)


# 删除
# del Student.country
# print(Student.country)
# 对属性的增添改查


def func(): pass


print("hello", func)
print(Student.learn)  # 访问类自己内的函数

# 调用的准寻函数的特性，函数有参数的限制； learn定义阶段是一个位置参数，意味着你在调用必须传值。不传就有问题啦
Student.learn('must to enter a value here ')

# 调用类的过程又称之为实例化

# 1, 得到一个返回值，即对象,该对象是一个空对象
# 2, 把调用类
stu2 = Student('Xiaoping', 28, 'Female')
stu1 = Student('Chipping', 18, 'Male')
# stu3 = Student()
# print(stu1.__dict__)
print('this student name is %s, His age is %d and his sex is %s' % (stu1.Name, stu1.Age, stu1.Sex))
print(stu2.__dict__)
print(stu2.Name, stu2.Age, stu2.Sex)
