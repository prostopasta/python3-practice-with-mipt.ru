n = []
flag_ok = False

for i in range(4):
    n.append(int(input()))

x = n[2] - n[0]
y = n[3] - n[1]

if (x == 0) or (y == 0) or (abs(x) == abs(y)):
    flag_ok = True

if flag_ok:
    print('YES')
else:
    print('NO')
