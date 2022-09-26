#!/usr/bin/env python
# -*- coding: utf-8 -*-
msg = 'hello everyone'
print(msg.count('e'))  # 统计字符串e出现的次数
print(msg.count('l', 1, 4))  # 字符串l在索引1~5范围内出现的次数

# 2, center,ljust,rjust,zfill
name = 'shiping'
print(name.center(30, '-'))  # 总宽度为30，字符串居中显示，不够用-填充
print(name.ljust(30, '*'))  # 总宽度为30，字符串左对齐显示，不够用*填充
print(name.rjust(30, '*'))  # 总宽度为30，字符串右对齐显示，不够用*填充
print(name.zfill(50))

# 3.expandtabs
name1 = 'shiping\tis such a good man'
print(name1)
print(name1.expandtabs(1)) #修改\t 制表符代表的空格数

#4 captalize,swapcese,title
#4.1 captalize 首字母大写
message='hello everyone nice to meet you!'
print(message.capitalize())
#4.2 swapcase 大小写翻转
message1='Hi girl, i want make fridends with you!'
print(message1.swapcase())

#4.3 title 每个单词的首字母大写
msg='dear my girlfriend i miss you very much !'
print(msg.title())
