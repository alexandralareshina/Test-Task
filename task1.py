n = int(input('Введите число n :'))
m = int(input('Введите число m :'))
a = []
res = []
# заполнение списка числами
for j in range(1, m ):
    for i in range(1, n + 1) :
        a.append(i)
# нахождение пути
for i in range (0, len(a), m -1):
    x = (a[i : i + m])
    cnt = res.count(1)
    if cnt < 2:
        res.append(x[0])
    else:
        res.pop()
        break
print(*res, sep='')
