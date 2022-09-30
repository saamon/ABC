h, w = map(int, input().split())
grid = []
# ここで入力を受け取る（二次元配列）
for _ in range(h):  # Nは行数
    a = list(map(int, input().strip().split()))
    grid.append(a)

# i1とi2,j1とj2について考える
# i1(0~H-1),i2(i1+1~H-1),j1(0~w-1),j2(j1+1~w-1)
for i1 in range(h):
    for i2 in range(i1, h):
        for j1 in range(w):
            for j2 in range(j1, w):
                if grid[i1][j1] + grid[i2][j2] > grid[i2][j1] + grid[i1][j2]:
                    print("No")
                    exit()
print("Yes")
