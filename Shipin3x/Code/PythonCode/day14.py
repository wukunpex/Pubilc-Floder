#!/usr/bin/env python
# -*- coding: utf-8 -*-
#列表

#定义：在 [] 内，用逗号分隔开多个任意数据类型的值
num=[1,'a',[1,2,]] #本质 num=list([1,'a',[1,2]])
print(num)

#4.2 类型转换
#但凡能被for循环遍历的数据类型都可以传给list()转换成列表类型，list()会跟for循环一样遍历出数据类型中包含
#的每一个元素然后放到列表中

print(list('chengshiping'))
print(list([1,2,3,4]))
print(list({'name':'shiping','age':13}))
print(list((1,2,3)))
print(list({1,2,3,4,5}))

#4.3 使用
#1, 按索引存取值（正向存取+反向存取）: 即可存也可以取
my_fridends=['shiping','xiaoming','xiaowang','xiaobing','xiaoming',4,5]
print(my_fridends[0]) #正向取(从左往右)

#1.2 反向取值（-负号表示从左往右）
print(my_fridends[-1])

#1.3 对于list来说，既可以按照索引取值，又可以按照索引修改指定的值，但如果索引不存在则报错
my_fridends[0]='male'
print(my_fridends)
print(len(my_fridends)) #长度

#4成员运算in 和not in
print('shiping' in my_fridends)
print('shiping' not in my_fridends)

#添加
#5.1 append() 列表尾部追加元素
list1=['a','b','c','d']
list1.append('f')
print(list1)

#extend() 一次性在列表尾部添加多个元素
list1.extend(['e','g','h','j'])
print(list1)

#5.3 insert() 在指定位置插入元素
list1.insert(0,'first') #0表示按索引位置插值
print(list1)

#5.4 del
demo=[1,2,3,4,5]
del list1[0]
del demo[4]
print(demo)
print(list1 )

#6.2 pop() 默认删除列表最后一个元素，并将删除的值返回，括号内可以通过加索引值来指定删除元素
demo1=[1,2,3,4,5,6]
res=demo1.pop() #默认删除列表最后一个元素
print(res)

res1=demo1.pop(1) #通过索引值来指定删除元素
print(res1)

#6.3remove() 括号内指名道姓表示要删除那个元素，没有返回值
print(demo1.remove(3))

#7, reverse() 颠倒列表内元素顺序
list2=[2,3,1,5,4,8,7,0,34,12]
list2.reverse()
print(list2)

#8 sort() 给列表内所有元素排序
#8.1 排序时列表元素之间必须是相同数据类型，不可混搭，否者报错哦
list3=[3,4,1,2,55,34,23,12]
list3.sort()
print(list3)

list3.sort(reverse=True) #reverse用来指定是否跌倒排序，默认为false （数字大到小排列 ）
print(list3)