x, y, r = map(int, input().split())

if (x**2 + y**2)**0.5 <= r:
    print("YES")
else:
    print("NO")
