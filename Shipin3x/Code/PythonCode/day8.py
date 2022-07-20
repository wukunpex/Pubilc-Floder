# 3.3.4 for loop application cases
# simple 1
for count in range(6):
    print(count)

# simple complex
count = 0
while count < 6:
    print(count)
    count += 1

# simple 2 for dirctory
for k in {'name': 'shiping', 'age': 18, "gender": 'male'}:
    print(k)
attribute = {'name': 'shiping', 'age': '27', 'gender': 'male'}
print(attribute['name'])

for i in range(3):
    for j in range(5):
        print("*", end='')
    print()

# exercise
for i in range(1, 10):
    for j in range(1, i + 1):
        print(' %s*%s=%s' % (i, j, i * j), end='')
    print()

# instance demo
max_level = 5
for current_level in range(1, max_level + 1):
    for i in range(max_level - current_level):
        print(' ',end='')
    for j in range(2*current_level-1):
        print('*',end='')
    print()

