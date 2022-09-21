N = int(input())
x, y = [], []

# 二次元座標の受け取り
for _ in range(N):
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)

ans = 0

for i in range(N):
    for j in range(i + 1, N):
        if abs(y[j] - y[i]) <= abs(x[j] - x[i]):
            ans += 1
print(ans)
