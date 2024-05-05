import random

a = []
for i in range(5):
    a.append(random.randint(1, 5))
b = int(input("введите число "))
n = 0
for i in a:
    if b == i:
        print("Поздравляю, Вы угадали число!", a)
        n = n + 1
        break
if n < 1:
    print("Нет такого числа!", a)
