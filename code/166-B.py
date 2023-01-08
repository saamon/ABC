N, K = map(int, input().split())
treat = set()

for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        treat.add(a)
print(N - len(treat))
