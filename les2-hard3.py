tower = []
sector = 1
spos = 0
for i in range(1,100):

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
    print (r)

num = 0
floor = 0

room = int(input("Введите номер комнаты: "))
for t in tower:
    if t.count(room) == 1:
        floor = tower.index(t)+1
        num = t.index(room)+1

print ("Этаж {}, расположение комнаты - {} слева".format(floor, num))