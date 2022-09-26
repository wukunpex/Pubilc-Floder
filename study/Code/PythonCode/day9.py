#!/usr/bin/env python
# -*- coding: utf-8 -*-
#5.2.1 digital tpye integer and float
#2.2 类型转换

s='123'
res=int(s)
print (s,type(res))

ss='123.3241'
res1=float(ss)
print(ss,type(res1))
#数字类型主要就是用来做数学与比较运算，因此数字类型除了与运算符结合使用之外，并无需要掌握的内置方法

variable=[1,2,3,4,5,6,7]
str1='shi ping!'
list={'name':'shiping','age':10,'gender':'male'}
print(type(list))
print(type(variable))
vari=str(variable)
print (type(vari))
CHlist=str(list)
print(type(CHlist))
print(type(str1[3]))

#  切片
print(str1[0:8]) #取出索引为0到8的所以字符
print(str1[0:9:2]) #第三个参数2代表步长，会从0开始，每次累加一个2即可，所以会取出索引0.2.4.6.8的字符
print(str1[::-1]) #反向切片 -1 表示从右往左依次取值
 #长度len
 #获取字符串的长度，即字符的个数，但凡存在于引号内的都算作字符
print(len(str1))

#成员运算in和ont in
#判断shi是否不在str1里面
print('shi' in (str1))
print ('shi' not in (str1))
true1='shi' in (str1)
print(true1)

list1=[1,24,4,5,6,7]
print(list1[0:])

#2 lower(),upper()
print(str1.lower())