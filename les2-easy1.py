fruitlist = ["яблоко", "банан", "киви", "арбуз"]
print("Дано: ", fruitlist)
print("Вывод:")

n = 1

for c in fruitlist:
    print(str(n) + ".", "{:>7}".format(c))
    n += 1

print("\n\nГОТОВО!")
