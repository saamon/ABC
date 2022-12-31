n, k, m = map(int, input().split())
a = list(map(int, input().split()))

sumA = sum(a)
ans = (n * m - sumA)  # n * m - 今までの点数

if ans > k:
    ans = -1
elif ans < 0:
    ans = 0

print(ans)
