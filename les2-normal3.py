import random

n = int(input("Сколько элементов должно быть в списке? "))
i = 0
list = []
while i < n:
    list.append(random.randint(-100, 100))
    i += 1
print (list)


print("\n\nГОТОВО!")