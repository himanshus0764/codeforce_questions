s = input()
t = input()
for i in range(len(s)):
    if s[i] != t[len(t) - 1 - i]:
        print("NO")
        break
else:
    print("YES")
