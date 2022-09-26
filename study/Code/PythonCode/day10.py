#!/usr/bin/env python
# -*- coding: utf-8 -*-
#strip 移除字符串首尾指定的字符（默认移除空格）
#5.1 括号内不指定字符，默认移除首位空格
str1=' life is short !  '
print (str1.strip())
#5.2 括号内指定字符，移除首尾指定的字符
str2='****shiping********'
#6 切分split
#6.1 括号内不指定字符，默认以空格作为切分符号
str3='heLlo sHipng'
print(str3.split())
#6.2 括号内指定分隔字符，则按照口号内指定的字符切割字符串
str4='127.0.0.1'
print(str4.split('.'))

#7.循环
str5='how are you today ?'
for i in str5:
    print(i,end='')
print()

#3.3.2
#strip lstrip rstrip
print(str2.strip('*'))
print(str2.lstrip('*'))
print(str2.rstrip('*'))

#2,lower(),upper()
#将英文字符串全部变小写
print(str2.lower())

#将英文字符串全部变大写
print(str2.upper())

# 3 startswith ,endswith
str6='tony jam'
print(str6.startswith('tony j')) #srartswith()判断字符串是否以括号内指定的字符开头，结果为布尔值True或False

print(str6.startswith('o'))

#endswith()判断字符串是否以括号内指定的字符结尾，结果为布尔值true or false
print(str6.endswith('jam'))
print(str6.endswith('tony'))