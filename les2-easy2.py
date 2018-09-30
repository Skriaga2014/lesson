
import random

list1 = [random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7)]
list2 = [random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7)]

print(list1)
print(list2)

list3 = []

for r in list1:
    if list2.count(r) == 0:
        list3.append(r)

if list3 == []:
    print ("В первом списке все числа совпадают с числами из второго списка")
else:
    print ("Осталось:", list3)

