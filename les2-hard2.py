
date = input ("Введите дату: ")

day = date[0:2]
mon = date[3:5]
yr = date[6:10]

if len(date) == 10:
    print ("Проверка на длину даты пройдена УСПЕШНО")
    if day.isdecimal() and mon.isdecimal() and yr.isdecimal() and date[2] == "." and date[5] == ".":
        print ("Проверка на число и точки пройдена УСПЕШНО")
        if int(day) <= 31 and int(mon) <= 12 and int(yr) > 0:
            print ("Проверка на соответствие чисел диапазону пройдена УСПЕШНО")
            if int(day) != 31 or [1,3,5,7,8,10,12].count(int(mon)) == 1:

                 print("ВСЁ ВЕРНО! Формат даты соответствует необходимому формату!")

            else:
                print("ОШИБКА! В месяце {} не может быть 31 день".format(mon))
        else:
            print ("ОШИБКА! Числа не входят в диапазон дат")
    else:
        print("ОШИБКА! Недопустимые символы")
else:
    print("ОШИБКА! Не соответствует длине корректной даты")

