#!/usr/bin/env python
# -*- coding: utf-8 -*-
#五元组
#元组与列表类似，也是可以存多个任意类型的元素，不同之处在于元素不能修改
#即元组相当于不可变的列表，用于记录多个固定不允许修改的值，单纯用于取
#5.2 定义方式
#在（）内用逗号分割开多个任意类型的值
countries=('chain','america','india','english') #本质 countries=tuple（'chain'...）
print(countries)
#元组内只有一个值，则必须加一个逗号，否则（）就只是包含的意思而非定义元组
countries1=('chain',)
print(countries1)
#类型转换
tuple('abcde')
tuple([1,2,3,4,5])
tuple({'name':'shiping','age':18})
tuple((1,2,3,4,5,6,7,8))
tuple({1,2,4,6,7,8})
#tuple（）会跟for循环一样遍历出数据类型中包含的每一个元素然后放到元组中
for i in tuple((1,2,3,4,5,6)):
    print(i,end="")

#六字典
#定义方式
#每个元素都是key:value的形式
info={'name':'shiping','age':12,'role':'handsomeman'}
#也可以这么定义字典
info1=dict(name='shiping',age=18,sex='male')
print(type(info1),info1)

#6.2 类型转换
#转换1：
info2=dict([['name','shiping'],('age',18),('sex','male')])
print(type(info2),info2)

#转换2 fromkeys 会从元组中取出每个值当做key，然后与None 组成Key:value 放到字典中
print({}.fromkeys(('name','age','sex'),None))
print(info2.fromkeys(('name','age','sex'),None))