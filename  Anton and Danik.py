num=int(input())
n=input()
a=n.count("A")
d=n.count("D")
if(a>d):
    print("Anton")
elif(a==d):
    print("Friendship")
else:
    print("Danik")