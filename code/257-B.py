N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for l in L:
    l -= 1
    if A[l] == N:
        continue
    elif l + 1 == K:
        A[l] += 1
    # 右にコマがないならば
    # A[l+1] - A[l] > 1
    elif A[l + 1] - A[l] > 1:
        A[l] += 1
print(*A)
