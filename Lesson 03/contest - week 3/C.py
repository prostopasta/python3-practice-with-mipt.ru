num = int(input())
flag = False

if (num % 100 == 0) and not (num % 400 == 0):
    flag = False
elif num % 4 == 0:
    flag = True

if flag:
    print('YES')
else:
    print('NO')
