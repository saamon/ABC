N = int(input())
d = list(map(int, input().split()))

ans = 0
# N * N -1 通りを全探索
for i in range(N + 1):
    for j in range(i + 1, N):
        ans += d[i] * d[j]
print(ans)
