#!/usr/bin/env python
# -*- coding: utf-8 -*-
# datetime: 9/22/2022 10:32 AM
# Software: PyCharm
# a.xml 有三个子标签
from xml.etree import ElementTree

# ElementTree.parse('a.xml')
tree = ElementTree.parse('a.xml')
root = tree.getroot()

print('first output', root)  # 一个元素(element) < Element 'data' at 0x000001DABF5A6400>
# 拿到一个元素需要掌握三个点
# 1,
# 第一个需要掌握的点叫tag,而得到的是标签的名字 data.
print('================1', root.tag)

# 2,
# 第二个需要掌握的叫attrib
print('================2', root.attrib)  # {'v': '1.0'} 添加一个属性 v=1.0

# 3,
# 第三个需要掌握的叫text
print('================3', root.text)

# 三种方式查找
# 从当前节点的子节点去找
print(root.find('country'))  # 只找一个
print(root.findall('country'))  # 找全部(多个)
print('====================find rank from data=============', root.find('rank'))  # 结果为None, ，所以用迭代器去找root.iter
# 从树形结构中查找
print(root.iter('rank'))  # 迭代器
print(list(root.iter('rank')))  # 迭代器，查看里面的内容

for country in root.findall('country'):
    rank = country.find('rank')
    year = country.find('year')
    print(rank.tag, rank.attrib, rank.text)
    print(year.tag, year.attrib, year.text)

# 需求把所有的a.xml 文档数据都打印出来，遍历文档树
for item in root:  # 取root的下一级
    print('==============iter document', item)

for country in root:
    # print('==========', country.tag)
    print('==========', country.tag, ':', country.attrib['name'], '==========')  # 知道国家了，在基于国家的元素继续走
    for item in country:  # 取出一个国家后
        print('print each country child nodes:', item.tag, item.attrib, item.text,
              '\n')  # 打印每个国家下面的子节点，打印每个子节点的tag,attrib,text

# 查找year 下边的值
for year in root.iter('year'):
    print('===============================',
          year.tag, year.attrib, year.text,
          '===============================')

# 修改a.xml or 写到b.xml
'''
首先找到
'''
for year in root.iter('year'):
    # 修改属性
    year.set('years', "1")  # 会得到一个全新的文件树. ()里面必须都是字符串类型
    year.text = str(int(year.text) + 89)  # 年的更新 数值""
tree.write('b.xml')  # 写到文件里面去

# 添加一个子节点
# 先要找到父节点

for country in root:
    obj = ElementTree.Element('shipping')  # 创建一个 <shipping name='shipping' age='29'> shipping is good</shipping>
    obj.attrib = {'name': 'shipping', 'age': '29'}
    obj.text = 'shipping is good'
    country.append(obj)
tree.write('c.xml')
