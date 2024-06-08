T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    max_repeating_count = max((A.count(x) for x in set(A)))

    if max_repeating_count % 2 == 0:
        print("Bob")
    else:
        print("Alice")
