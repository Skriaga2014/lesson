tower = []  #список списков
sector = 1  #сектор комнат (Сектор 4 - 4 этажа по 4 комнаты)
spos = 0    #номер комнаты в секторе (номер вышел за пределы сектора - новый сектор)


for i in range(1,100):      #100 - количество комнат в доме

    if tower == []:
        tower.append([i])
        spos = 1
    else:
        if spos == 1:
            tower.append([i])
            spos +=1
            sector += 1
        elif 1 < spos < sector**2:
            if len(tower[-1]) == sector**2/sector:
                tower.append([i])
                spos += 1
            else:
                tower[-1].append(i)
                spos += 1
        else:
            tower[-1].append(i)
            spos = 1




for r in reversed(tower):
    ttt = len(str(tower.index(r)+1))                                #длина номера этажа
    rrr = (len(str(tower[-2]))-len(str(tower[tower.index(r)])))//2  #половина разницы между длины самой длинной строки и текущей строки
    print (str(tower.index(r)+1) + "." * (5-ttt+rrr), r)

num = 0
floor = 0

room = int(input("\n Введите номер комнаты: "))
for t in tower:
    if t.count(room) == 1:
        floor = tower.index(t)+1
        num = t.index(room)+1

print ("Этаж {}, расположение комнаты - {} слева".format(floor, num))
#