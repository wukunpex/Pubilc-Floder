#!/usr/bin/env python
# -*- coding: utf-8 -*-
# datetime: 9/21/2022 9:51 AM
# Software: PyCharm
import configparser

# 得到一个对象
config = configparser.ConfigParser()

# 从硬盘读到内存，读.ini文件
config.read('my.ini')

print(config.sections(), '\n')  # 打印有哪些section ['terminal', 'client']
print('list client options of client', config.options('client'))  # 看对应的section 有那些options ['user', 'password']
print('list client options of terminal', config.options('terminal'))  # 看对应的section 有那些options ['user', 'password']
# 获取option 标题下的对应的值
print(config.get('terminal', 'port'))

# 假如这个配置项没有就会报错
# 有一个配套的东西可以判断有没有
# print(config.has_option('terminal', 'aaaa'))
if config.has_option('terminal', 'aaaa'):
    print(config.get('terminal', 'aaaa'))

# print(config.get('terminal', 'ssss'))  # configparser.NoOptionError: No option 'ssss' in section: 'terminal'

print('===========', type(config.get('terminal', 'default-engine')))  # 当前的不是一个真的bool值，实际是一个字符串 <class 'str'>
# 可以用一个bool去转换并查看 <class 'bool'>
print(bool(config.get('terminal', 'default-engine')))
print('===========', type(bool(config.get('terminal', 'default-engine'))))

# 直接一步到位，拿到就是bool值
# print(config.getboolean('terminal', 'skip-gran-table'))

# 通过getint 拿数字类型，而不是一个字符串
print(type
      (config.getint('terminal', 'port')),
      (config.getint('terminal', 'port')),
      )
# 通过getfloat 拿浮点类型，而不是一个字符串
print(type
      (config.getfloat('terminal', 'port')),
      (config.getfloat('terminal', 'port')),
      )

# 也可以添加section 到my.ini 文件
# config.add_section('shipping')
# config.set('shipping', 'name', 'chipping')  # 1,section; 2, option; 3,value; 必须是字符串，目前只在内存中，没有写道文件
# config.set('shipping', 'age', '18')
# # 如果要写到my.ini 文件中
# config.write(open('my.ini', 'w', encoding='utf-8'))

# 修改原本my.ini 文件中的值
config.set('shipping', 'age', '29')
config.write(open('my.ini', 'w', encoding='utf-8'))
