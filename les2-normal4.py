import random

list = []
for i in range(1,11):
    list.append(random.randint(1,5))

print("Дан список:", list)

list1 = []
list2 = []
for n in list:
    if list1.count(n) == 0:
        list1.append(n)

for n in list:
    if list.count(n) == 1:
        list2.append(n)

print ("Неповторяющиеся элементы исходного списка:", list1)
if list2 == []:
    print ("Элементов исходного списка, которые не имеют повторений, не найдено")
else:
    print ("Элементы исходного списка, которые не имеют повторений:", list2)

#