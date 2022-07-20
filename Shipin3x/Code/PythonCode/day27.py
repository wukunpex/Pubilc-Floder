#!/usr/bin/env python
# -*- coding: utf-8 -*-
def functionname(arg1,arg2,**vardict):
    print("output")
    print(arg1,'\n',arg2)
    print(vardict)
functionname(1,"a",b=2)

def f (a,b,c,*,d):
    return a+b+c+d
print(f(1,2,3,d=0))

#return 语句
#可写函数说明
def sum(arg1,arg2):
    total=arg1+arg2
    print('returns the total of in function ',total)
    return total
total= sum(10,30)
print ("out funcation",total)

n =100
sum = 0
counter = 1
while counter <=n:
    sum=sum+counter
    counter +=1
print('1 to %d sum as %d' % (n,sum))

count =0
while count < 5:
    print(count,"less than 5")
    count =count +1
else:
    print(count,"great than or eq than 5")

for i in range(90,999,3):
    print(i)

a = ['google','IE','runoob','taobao','qq']
for i in range(len(a)):
    print(i,a[i])