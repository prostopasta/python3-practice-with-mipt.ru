x = int(input())
maximal = x
count = 0
while x != 0:
    if (x == maximal):
        count += 1
    elif (x > maximal):
        maximal = x
        count = 1
    x = int(input())

print(count)
