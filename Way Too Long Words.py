for i in range(int(input())):
    a = input()
    b = len(a)
    result = a[0] + str(b-2) + a[b-1]
    if b<11:
        print(a)
    else:
        print(result)
