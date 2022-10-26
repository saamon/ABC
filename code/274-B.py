H, W = map(int, input().split())
grid = []

for i in range(H):
    C = input()
    # 一文字ずつ格納するためリストに変換する
    C = list(C)
    grid.append(C)

ans = []

# 外側のループ->内側のループ
for w in range(W):
    count = 0
    for h in range(H):
        if grid[h][w] == "#":
            count += 1
    ans.append(count)

print(*ans)
