x, p, y = map(float, input().split())
deposit = x
n = 0

while deposit < y:
    deposit += int(deposit * p) / 100
    n += 1

print(n)
