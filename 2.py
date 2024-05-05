import random

a = []
for i in range(10):
    a.append(random.randint(1, 10))
print(a)
for i in range(10):
    if a.count(i) > 1:
        print(i)

