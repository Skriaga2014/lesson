
print("Welcome to homework number 2: Easy")
print("press 1 for task \"Fruits list\"")
print("press 2 for task \"Two lists\"")
print("press 3 for task \"Number list\"")
a = input()

if a == "1":
    fruitlist = ["яблоко", "банан", "киви", "арбуз"]
    print("Дано: ", fruitlist)
    print("Вывод:")

    n = 1

    for c in fruitlist:
        print(str(n) + ".", "{:>7}".format(c))
        n += 1

elif a == "2":
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

elif a == "3":

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

