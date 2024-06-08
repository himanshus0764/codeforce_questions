k,n,w=map(int,input().split())
m=1
sum=0
for i in range(w):
    sum+=(k*m)
    m+=1
h=(sum-n)
if h<0:
    print(0)
else:
    print(h)