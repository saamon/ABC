# 二次元配列 ([i][j]にアクセスするために)
# 入力を受け取る
A = []
for i in range(10):  # Nは行数
    S = input()
    A.append(S)

a = c = 100  # 最小値
b = d = 0  # 最大値

for i in range(10):
    for j in range(10):
        if A[i][j] == "#":
            # インデックスがずれる(+1する)
            a = min(a, i + 1)
            b = max(b, i + 1)
            c = min(c, j + 1)
            d = max(d, j + 1)
print(a, b)
print(c, d)
