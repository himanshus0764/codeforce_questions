a, b = map(int, input().split())

for _ in range(b):
    if a % 10 != 0:
        a -= 1
    else:
        a //= 10
print(a)
