a,b=map(int,input().split())
c=0
while True:
    if a>b:
        break
    else:
        c+=1
        a*=3
        b*=2
print (c)
