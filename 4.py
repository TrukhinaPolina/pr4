import random

a = ['Алексеев', 'Иванов', 'Павлов', 'Козлов', 'Степанова', 'Николаев', 'Орлова', 'Андреев', 'Макаров', 'Никитина']
b = ['Киселева', 'Ильин', 'Максимов', 'Поляков', 'Виноградов', 'Ковалев', 'Медведев', 'Антонов', 'Тарасов', 'Жуков']
c = []
n = 0
k = 0
print(" исходные списки групп:");
print(a)
print(b)
while n < 5:
    c.append(a[random.randint(0, 9)])
    c.append(b[random.randint(0, 9)])
    n += 1
c = tuple(c)

print("спортивная команда", c)
print(len(c))
print(sorted(c))
for c in c:
    if c == "Иванов":
        k = k + 1
        print("Иванов есть")
        break
    else:
        print("Иванова нет")
        break

print(k)
