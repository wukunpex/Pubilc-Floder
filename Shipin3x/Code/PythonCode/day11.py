#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 4, 格式化输出之format
# 之前我们使用%s 来做字符串的格式化输出操作，在传值时，必须严格按照位置与%s 一一对应，而字符串的内置方法format 则提供了一种
# 不依赖位置的传值方式
str = 'my name is {name}, my age is {age} !'.format(age=18, name='shiping')
print(str)
str1 = 'my name is {name}{name}{name}, my age is {age}'.format(name="suck a nice man", age=18)
print(str1)
# format 另一种使用方式
# 类似于%s的方法，传入的值会按照位置与{} --对应
str2 = 'my name is {},my age is {}'.format('babycheng', 18)
print(str2)

# format 传入的多个值当作一个列表，然后用{索引}取值
str3 = 'my name is {0}, my age is {1}'.format('cheng', 18)
print(str3)
str4 = 'my name is {1}, my age is {1}'.format('pingping', 18)
print(str4)

# split 会按照从左到右的顺序对字符串进行切分，可以指定切割次数
str5 = 'c:/temp/file/log/sublog/log.txt'
print(str5.split('/', 3))

# rsplit刚好与split相反，从右往左切割，可以指定切割次数
str6 = 'a|b|c|e|f|g|h|i|j|k|l'
print(str6.rsplit('|', 3))

# 6.join
# 从可迭代对象中取出多个字符串，然后按照指定的分割符精心发拼接，拼接的结果为字符串
print('%'.join('hello'))  # 从字符串hello 中取出多个字符串，然后按照%作为分隔符号拼接

print('|'.join(['shiping', '18', 'computergame']))  # 从列表中取出多个字符串，然后按照|作为分隔符号进行拼接

# 7replace
#用新的字符替换字符串中旧的字符
str7='my name is shiping, my age is eighteen'
print(str7)
str7=str7.replace('shiping','huck') #语法 replace（'旧的内容'，'新的内容'）
print(str7)

#可以指定修改的个数
str7=str7.replace('my','MY',1)#只把一个my改为MY
print(str7)

#8 lsdigital 判断字符串是不是纯数字组成，返回结果为True or False
str8='2387483'
print(str8.isdigit())

#3.3.3 了解操作
#1,fand ,rfind,index,rendex,count
#1.1 find 从指定范围内查找子字符串的起始索引，找得到则返回数字1，找不到则返回-1
msg='shiping say hello !'
print(msg.find('g',0,7)) #在索引为1和2(骨头不顾尾)的字符中查找字符G的索引
#1.2 index 同find，但在找不到时会报错
print(msg.index('y',1,5))


