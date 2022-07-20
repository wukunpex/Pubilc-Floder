#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python while 循环语句
a = 1
while a < 10:
    print (a)
    a += 2
numbers = [12,13,45,46,67,44,88,0]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if(number % 2 == 0 ):
        even.append(number)
        print('even',number)
    else:
        odd.append(number)
        print('odd',number)


i = 1
while i < 10:
    i += 1
    if i%2 > 0:
        continue
    print (i)
print('#############################')
i = 1
while "1":
    print (i)

    i += 1
    if i > 10:
        break
var = 1
while var == 1:
    num = input("enter a number : ")
    print ("your entered: ", num)
    break
print ("good bye")
print("###########################################")
for cheng in range (10,20):
    for i in range(2,cheng):
        if cheng%i == 0:
            j=cheng/i
            print('%d eq %d * %d' % (cheng,i,j))
            break
    else:
        print(cheng,"is a even number")