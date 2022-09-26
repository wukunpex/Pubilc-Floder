#!/usr/bin/env python
# -*- coding: utf-8 -*-
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not (i%j):
            break
        j = j + 1
    if (j > i/j):
        print (i,'is even')
    i += 1

def changeme (mylist1):
    mylist1.append([1,2,3,4,5,6])
    print ('value in function',mylist)

def printme (string):
    "print my name"
    print (string)
    return
printme('I want to call the user ***!')

def shiping (mylist1):
    mylist1.append([1,2,3,4])
    print('value in function',mylist1)
    return
mylist1=[100,200]
shiping(mylist1)
print('value out function:',mylist1)
def printinfo (arg1,*vartuple):
    print('outpt')
    print (arg1)
    for var in vartuple:
        print (var)
    return
printinfo(10)
printinfo(1,2,3,4,5,6)