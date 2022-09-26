#!/usr/bin/env python
# -*- coding: utf-8 -*-
timeStr = input("please enter the current time : ")
# 12:23:40
timeList = timeStr.split(":")
h = int(timeList[0])
m = int(timeList[1])
s = int(timeList[2])
s = s + 1

if s == 60:
    m += 1
    s=0
    if m == 60:
        h = h +1
        m =0
        if h == 24:
            h=0
print ("%.2d:%2d:%2d" % (h,m,s))