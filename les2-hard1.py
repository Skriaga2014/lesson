
equation = "y = -12x + 11111140.2121"
x = 2.5

print (equation)
print ("x =", x)

a = equation.split()
a[2] = a[2][:-1]

a[2] = float(a[2])

if a[3] == "-":
    a[3] = "+"
    a[4] = -float(a[4])
else:
    a[4] = float(a[4])

y = a[2] * x + a[4]

print("\n", a, "\n")
print("y =", y)

print("\n\nГОТОВО!")