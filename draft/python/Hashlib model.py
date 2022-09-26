#!/usr/bin/env python
# -*- coding: utf-8 -*-
# datetime: 9/20/2022 1:49 PM
# Software: PyCharm

"""
hash: 一种算法，3x里代替了md5模块和sha模块，主要提供 SHA1,SHA224,SHA256,SHA512
MD5 算法
三个特点：
1， 内容相同则hash 运算算法相同，内容稍微改变则hash 值则变
2，不可逆推
3，相同的算法，无论校验多长的数据，得到的哈希值长度固定

"""
import hashlib
import hmac

m = hashlib.md5()  # 调用MD5这个模块
m.update('this is to evaluate hash value'.encode('utf-8'))  # 校验之前必须是encode.必须给一个bits 类型才可以校验
m.update('this is to evaluate hash value demo'.encode('utf-8'))  # 校验之前必须是encode.必须给一个bits 类型才可以校验
m1 = hashlib.md5()  # 调用MD5这个模块
m1.update('this is to evaluate hash value'.encode('utf-8'))  # 校验之前必须是encode.必须给一个bits 类型才可以校验
m1.update('this is to evaluate hash value demo'.encode('utf-8'))  # 校验之前必须是encode.必须给一个bits 类型才可以校验
print(m.hexdigest(),
      '\n',
      m1.hexdigest(),
      )

m4 = hmac.new('加盐'.encode('utf-8'), digestmod='md5')
m4.update('cheng123'.encode('utf-8'))
print('m4', m4.hexdigest())

name = input('user:>>')
pwd = input('password:>>')
m = hashlib.md5()
m.update(pwd.encode('utf-8'))
pwd = (m.hexdigest())
# print('your username is %s and user password is %s', % (name, pwd))
print(name, pwd)

# 反推密文得出密码，暴力破解

cryt_pwd = 'd0601b37c1696e1022663e07269f80ae'
pwds = [
    'aeious123',
    '124124',
    'aeiou123',
    'sadaf123',
    'cheng1993',
]


def make_dic(pwds):
    dic = {}
    for pwd in pwds:
        m1 = hashlib.md5(pwd.encode('utf-8'))
        # m.hexdigest()
        dic[pwd] = m1.hexdigest()
    return dic


# print('list ', make_dic(pwds))

dic = make_dic(pwds)

print('type they attribution is', type(dic))

for pwd in dic:
    if dic[pwd] == cryt_pwd:
        print("password is:", pwd)
    else:
        print('the password %s is wrong' % dic)

# 针对这种情况怎么防止， 涉及到密码加盐，怎么密码加盐呢
m2 = hashlib.md5('密码加盐'.encode('utf-8'))  # 真正的解决方法是密码加盐
# m2 = hashlib.sha512()  # 512只是算法复杂加大，密文长度增加
m2.update('cheng1993'.encode('utf-8'))
m2.update('密码加盐'.encode('utf-8'))
print('m2 hash value', m2.hexdigest())
