n, h = map(int, input().split())
height = map(int, input().split())
c, b = 0, 0

for i in height:
    if i <= h:
        c += 1
    else:
        b += 2

print(c+b)
