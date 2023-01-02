n, m = map(int, input().split())
# 繋がっているかを確認する二次元配列
connect = [[False] * (n + 1) for i in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    # 繋がっている場所をTrueにする
    connect[u][v] = True
    connect[v][u] = True

ans = 0
for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        for c in range(b + 1, n + 1):
            # a,b,cが全て繋がっていれば+1
            if connect[a][b] == True and connect[b][c] == True and connect[c][a] == True:
                ans += 1
print(ans)
