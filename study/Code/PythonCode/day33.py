#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python3数据结构
#列表
a = [66.2, 43,123,23,44,55,23,33,12,12,3,3,8]
print(a.count(3),a.count(12),a.count(1))
a.insert(0,8)
a.append(99999999)
print(a)
print(a.index(3))
a.remove(33)
print(a)
a.reverse()
print(a)
a.sort()
print(a)


stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

from collections import deque
queue = deque(["Eric","John","Micheal"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)


#列表推导式
vec=[2,4,6]
print([3*x for x in vec])
print([[x,x**2]for x in vec])
freshfruit=['banana','loganberry','passion fruit']
print([weapon.strip() for weapon in freshfruit])
