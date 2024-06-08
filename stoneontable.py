a=int(input())
b=input()
count=0
for i in range(0,a-1):
    if b[i]==b[i+1]:
        count+=1
print(count)