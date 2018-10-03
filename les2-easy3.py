import random

list1 = []
for i in range(0, 10):
    list1.append(random.randrange(1, 10))
print(list1)

n = 0
for r in list1:
    if r%2 == 0:
        list1[n] = r/4
    else:
        list1[n] = r*2
    n += 1
print(list1)
#
