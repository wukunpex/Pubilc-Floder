# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# x='上'
# res=x.encode('utf-8')
# print(res,type(res))
# def auth_user():
#     '''user authentcation function'''
#     pass
# def download_file():
#     '''download file function'''
#     pass
#
#
# def test(x,y,z):
#     return x,y,z
# res=test('shiping',1,3)
# # test(1,2,3)
# print(res)
#
#
# # def register(name,age,sex):
# #     print('name is {name} age is {age} sex is {sex}'.format(name='shiping',age=28,sex='male'))
# #
# # register('shiping',27,'famale')
#
# var=1
# def foo(args=var):
#     print(args)
#
# var=6
# foo(4455555555555)

# def foo(n,arg=[]):
#     arg.append(n)
#     return arg
# foo(234222222222222)

# def foo(n,arg=[]):
#     arg.append(n)
#     return arg
# var=foo(23)
# var=foo(234)
# print(var)
# def func(n,args=None):
#     if args is None:
#         arg=[]
#     arg.append(n)
#     return arg
# print(func)
# res=func(1)
# print(res,type(res))

# def var(x,y,z,*arg):
#     # print(x)
#     # print(y)
#     # print(z)
#     # print(args)
#     print(x,y,z,arg)
# # var(1,2,3,4,5,6,7,87)
# # fun=var(1,2,3,4,5,6)
# # l=[1,2,3,4,5,6,7,8,9]
# var(1,2,3,4,5,6,7,8,9)
# def outer(x,y,z='shiping'):
#     print(x,y,z,)
# outer(*[1,2])
# print(outer)


# def add(*args):
#     res=0
#     for i in args:
#         res+=i
#     return res
#
# sum1=add(1,2,3,4,5,6,7,8,9)
# print(add)
# print(sum1)

#
# def func(x,**kwargs):
#     print(x)
#     print(kwargs)
#
# func(y=2,x='shiping',z=12,g='ship')
#
# def func(x,y,**kwargs):
#     print(x,y,kwargs)
#
# dic={'a':1,'b':'shiping'}
# func(1,2,**dic)
# def register(name,age,**args):
#     if 'sex' in args:
#         pass
#     if 'height' in args:
#         pass
#     return name
# res=register('shiping',28,region='chongqing',nationality='china')
# print(res)
# print(register)
# def register(name,age,*agrs,sex='male',height):
#     print('my name %s and age %d and sex %s and height %s'%(name,age,sex,height))
# register('shiping',1212,1222,2,222,12,height=180)
#
#
# x=100
# def func():
#     x=300
#     print(x)
# func()

# x=100
# def func():
#     pass
#     x=400 # 再函数调用时产生局部作用域的名字x
# func()
# print(func)
# print(x) #在全局找x，结果为100
#提示， 可以在调用内建函数local（）和globals（）来分别查看局部作用域和全局作用域的名字，查看的结果都是字典的格式，在全局作用域查看到的local
#的结果等于globals（）
#python 支持函数的嵌套定义，在内嵌的函数内查找名字时，会优先查找自己局部作用域的名字，然后由内而外一层层查找外部嵌套函数定于的作用域
#没有找到，则查找全局作用域
# x=1
# def outer():
#     x=2
#     def inner():
#         x=3
#         print('inner x:%s' %x)
#     inner()
#     print('outer x:%s' %x)
#
# outer()
# x=1
# def func():
#     global x
#     x='shiping'
#     print(x)
# func()
# print(x)
# num_list=['shiping',18,'chongqing']
# def func(nums):
#     nums.append('shanghai')
# func(num_list)
# print(num_list)
# def f1():
#     x=2
#     def f2():
#         nonlocal x
#         x=3
#     f2()
#     print(x)
#
# f1()
# def add(z,x):
#     return z+x
# func=add
# print(func(8,6))
# dic={'add':add,'max':max}
# print(dic)
# print(dic['add'](1,9))
#1.1函数可以被引用
# def add(x,y):
#     return x+y
# func=add
# print(func(1,2))

#1.2 函数可以作为容器类型的元素
# dic={'add':add,'max':max}#{'add': <function add at 0x00000278A78CB790>}
# print(dic)
# print(dic['add'](1,2))
#
# def foo(x,y,func):
#     return func(x,y)
#
# foo0=foo(12,22,add)
# print(foo0)
#
# def bar():
#     return add
# func=bar()
# print(func(1,6))

#2.1 闭于与包
x=1
def f1():
    def f2():
        print(x)
    return f2
def f3():
    x=3
    f2=f1()
    f2()
f3()
import requests
def get(url):
    return requests.get(url).text
get('https://www.python.org')