import random

list1 = [random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7)]
list2 = [random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7)]

print(list1)
print(list2)

for r in reversed(list1):
    if list2.count(r)>0:
        list1.remove(r)

if list1 == []:
    print ("В первом списке все числа совпадают с числами из второго списка")
else:
    print ("Осталось:", list1)
    #