# 2.4 逻辑运算符
# 2.4.1连续多个and
print(2 > 1 and 1 != 1 and true and 3 > 2)
print(2 > 1 and 1 != 1 and true and 3 > 2)
# 2.4.2 连续多个or
print(2 > 1 or 1 != 1 or true or 3 > 1)
# 2.4.3 混用and,or,not
print(3 > 4 and 4 > 3) or ((1 == 3 and 'x' == 'x') or 3 > 3)
print(not 'lili' in ['jack', 'tom', 'rubin'])
print('output keyword', 'lili' not in ['jack', 'lili', 'robin'])

# 2.6 身份运算符
x = 'info tony:18'
y = 'info tony:18'
print(type(x), type(y))
print(id(x), id(y))
