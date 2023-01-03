n = int(input())
w = list(map(int, input().split()))
ans3 = 100 * 100
for t in range(n):
    a = w[:t]
    b = w[t:]
    # スライスで両端から足していき最小値を求める
    ans3 = min(ans3, abs(sum(a) - sum(b)))
print(ans3)
