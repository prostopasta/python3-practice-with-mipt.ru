x = int(input())    # вводим натуральное N<=10000 , длина массива
num = 0             # количество 1, идущих подряд (без 0 между ними)
tmp = 0             # временный счетчик

while (x > 0) and (x < 10001):
    a = int(input())

    if a == 1:
        tmp += 1
    elif a == 0:
        tmp = 0
    else:
        break

    if tmp > num:
        num = tmp

    x -= 1

print(num)
