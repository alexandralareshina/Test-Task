import math
import re

def uravnenie_okr(ox, oy, rad, a, b):
    if pow((ox-a), 2) + pow((oy-b), 2) == pow(rad, 2):
        print(f"0 - точка {a},{b} лежит на окружности с центром {ox},{oy} и радиусом {rad}.")
    elif pow((ox-a), 2) + pow((oy-b), 2) > pow(rad, 2):
        print(f"2 - точка {a},{b} снаружи окружности с центром {ox},{oy} и радиусом {rad}.")
    else:
        print(f"1 - точка {a},{b} лежит внутри окружности с центром {ox},{oy} и радиусом {rad}.")


# получаем данные окружности из файла
f1 = open('file1.txt', 'r')

okr = list(map(int, re.split(" |,|/n", f1.readline())))
rad = int(f1.readline())
f1.close()
ox = okr[0]
oy = okr[1]

f2 = open('file2.txt', 'r')
t1 = list(map(int, re.split(" |,|/n", f2.readline())))
t2 = list(map(int, re.split(" |,|/n", f2.readline())))
t3 = list(map(int, re.split(" |,|/n", f2.readline())))
f2.close()
a1 = t1[0]
b1 = t1[1]
a2 = t2[0]
b2 = t2[1]
a3 = t3[0]
b3 = t3[1]

uravnenie_okr(ox, oy, rad, a1, b1)
uravnenie_okr(ox, oy, rad, a2, b2)
uravnenie_okr(ox, oy, rad, a3, b3)
