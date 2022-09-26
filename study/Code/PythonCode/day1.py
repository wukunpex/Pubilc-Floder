__author__ = 'shipin3x'
'''
#define variable
#integer and float variable showed
age = 18
birthday =1993
name = 'shiping'
height = 173.5
weight =74.7
a = 10
b = 30
c = a + b
b < a

print ("sum=",c,type(name),name,age,birthday,height,"tizhong=",weight)
'''
"""
python define list demo
as simple
"""
stu_nmaes=['zhang','shiping','cheng']
print (stu_nmaes[0])
"""
lisi can be nest
as example
"""
students_info = [['xiaoming',15,'age',19],['tony','nan'],18,['jack','hubbies','playbsll']]
print ('lll',students_info[3][1])
students_info1=['tony',18,['jack',]],['jason',10,['play','sleep']]
print ('kkkkk',students_info1[1][2][0])

"""
dictionary type demo
"""
students = [
    {'name':"shiping"},{'age':[27,'xiaozhang']},{"hobbies":'ball'}
]
print (students[1]['age'][1])
a = 19.0000
print (type(a),id(a),a)

"""
引用计数扩展阅读
"""
l1=['xxx']
l2=['yyy']
l1.append(l2)
l2.append(l1)
print (l1)
print (l2)

print ('answer',l1[0])
print (l1[1])
print (l1[1][1])
print (l1[1][1][1])
print (l1[1][1][1][1][0])
print (l2[0])