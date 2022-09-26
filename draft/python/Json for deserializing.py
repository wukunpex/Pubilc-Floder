#!/usr/bin/env python
# -*- coding: utf-8 -*-
# datetime: 25/09/2022 22:11
# software: PyCharm
import json

with open('user.json', 'r', encoding='utf-8') as f:
    # print(f.read())  # {"name": "Shipping", "age": 18, "nb": true}
    user = json.loads(f.read())  # 对应dumps
    print(user['name'])

# 一步搞定方法
json.load(open('user.json', 'r', encoding='utf-8'))  # load 对应dump 操作
print(user['age'])
print(user['nb'])

json_str = '{"sex":"female"}'
# json_str = "{'sex':'female'}"  # json 格式不能用单引号，他识别不了字符串

print(json.loads(json_str)['sex'])
