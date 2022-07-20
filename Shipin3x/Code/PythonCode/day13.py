#!/usr/bin/env python
# -*- coding: utf-8 -*-
#5 is 数字系列
num1=b'4' #byte
num2=u'4' #unicode
num3='四' #中文
num4='Ⅳ' #罗马数字

#isdigt ;bytes,unicode
print(num1.isdigit())
print(num4.isdigit())
print(num2.isdigit())

#isdecimal; uncicode(bytes类型无isdecimal方法)
print(num2.isdecimal())
print(num3.isdecimal())
print(num4.isdecimal())
#isnumberic:unicode 中文数字，罗马数字（bytes类型无isnumberic方法）
print(num2.isnumeric())
print(num3.isnumeric())
print(num4.isnumeric())

#三者不能判断浮点数
num5='4.4'
print(num5.isdigit())
print(num5.isdecimal())
print(num5.isnumeric())

'''
最常用的是isdigit，可以判断bytes 和unicode类型，这也是最常见的数字应用场景如果要判断
中文数字或罗马数字，则需要用到isnumberic
'''

#is其他
name1='Shiping123'
print(name1.isalnum()) #字符串中即可以包含数字也可以包含字母
print(name1.isalpha()) #数字中只包含字母
print(name1.islower()) #字符串是否纯小写
print(name1.isupper()) #字符串是否是纯大写
print(name1.isspace()) #字符串是否全是空格
print(name1.istitle()) #字符串中的单词首字母是否都是大写

