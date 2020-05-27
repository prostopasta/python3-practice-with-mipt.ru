"""
Контест 1 неделя: D - Обработка массива чисел

На вход программа получает набор чисел, заканчивающихся решеткой. Вам требуется найти: среднее, максимальное и
минимальное число в последовательности. Так же нужно вывести cумму остатков от деления суммы троек на последнее число
тройки (каждые 3 введеных числа образуют тройку). Для понимания рассмотрим пример входных данных: 1 2 3 4 5 6
среднее: (1 + 2 + 3 + 4 + 5 + 6) / 6 = 3.5 максимум: 6 минимум: 1 сумма остатков троек: (1 + 2 + 3) mod 3 + (4 + 5 +
6) mod 6 = 6 mod 3 + 15 mod 6 = 0 + 3 = 3 Среднее выводить, округлив до трех знаков после запятой. Для этого нужно
использовать функцию round(x, 3) Того ваша программа должна вывести: 3.5 6 1 3 Подумайте, имеет ли смысл хранить всю
последовательность.

Формат входных данных Последовательность чисел, заканчивающися '#'. Все числа от 1 до 100. Количество чисел в
последовательности кратно трем. Одно число на строку.

Формат выходных данных
Четыре числа, разделенных пробелом.
"""

mini = 101  # минимум
maxi = 1    # максимум
medi = 0    # среднее
mod3 = 0    # cумма остатков от деления суммы троек на последнее число тройки (каждые 3 введеных числа образуют тройку)
num = 0     # кол-во чисел в последовательности
tmp = 0     # сумма троек

while True:
    try:
        x = input()    # вводим натуральное 0<=N<=100 - набор чисел, заканчивающихся решеткой
    except Exception:
        exit(1)

    try:
        if str(x) == "#":
            if num % 3 == 0:
                break
            else:
                continue
    except TypeError:
        continue
    except ValueError:
        continue
    except Exception:
        exit(1)

    try:
        x = int(x)
    except TypeError:
        continue
    except ValueError:
        continue
    except Exception:
        exit(1)

    if (x <= 0) or (x > 100):
        continue

    num += 1
    medi += x

    if x < mini:
        mini = x

    if x > maxi:
        maxi = x

    if num % 3 == 0:
        mod3 += (tmp % x)
        tmp = 0
    else:
        tmp += x

if num == 0:
    num = 1
    mini = 0

print(round(medi / num, 3), maxi, mini, mod3)