# 行ごとに計算したリスト
# 列ごとに計算したリスト

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
# 行と列ごとの合計をリストに入れる
sum_row = list(map(sum, A))  # 行
sum_col = list(map(sum, zip(*A)))  # 列

for i in range(H):
    for j in range(W):
        A[i][j] = sum_row[i] + sum_col[j] - A[i][j]  # 被っている場所を削除

# 出力
for i in range(H):
    print(*A[i])
