#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 计算面颊函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("welcome", name)


print_welcome("Runoob")
w = 5
h = 4
print("width=", w, "heiht=", h, "area=", area(w, h))


def sum(arg1, arg2):
    total = arg1 + arg2
    print("in function: ", total)
    return


# call a funcrion
total = sum(10, 20)
print("out function: ", total)


