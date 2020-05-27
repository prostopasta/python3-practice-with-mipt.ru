x, p, y = map(float, input().split())
sum = x
n = 0

while sum < y:
    sum += int(sum * p) / 100
    n += 1

print(n)
