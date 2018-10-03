import random
import math

list1 = []
list2 = []

a = 0
while a < random.randrange(10,20):
    list1.append(random.randrange(1,100))
    a += 1
print ("Дано:", list1)

for i in list1:
    if math.sqrt(i)%1 == 0:
        list2.append(int(math.sqrt(i)))

if list2 == []:
    print("В списке нет чисел, из которых можно извлечь корень")
else:
    print ("Результат:", list2)
#