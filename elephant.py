m = [5, 4, 3, 2, 1]
n = int(input())
c = 0

for value in m:
    if n >= value:
        count = n // value
        n -= count * value
        c += count

print(c)
