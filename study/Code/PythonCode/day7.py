#!/usr/bin/env python
# -*- coding: utf-8 -*-
#案例五 while+else 的使用
#在while循环的后面，我们可以跟else 语句，当while循环正常执行完成并且中间没有break
#终止的话，就会执行else后面的语句，所以我们可以用else来验证，循环是否正常结束
count=0
while count <=5:
    count +=1
    print ("loop",count)
else:
    print("the loop has performed finished !")
#exercise 1
#寻找1到100 之间的数字7最大的倍数
number=100
while number >0 :
    if number%7==0:
        print(number)
        break
    else:
        number -=1

    #exercise 2
    age = 18
    count=0
    while count<=3:
        count+=1
        guess = int(input(">>:"))
        if guess >age:
            print("wow, you guessed so right")
        elif guess<age:
            print("too small ")
        else:
            print("Congratulations, you guessed it right")
