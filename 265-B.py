N, M, T = map(int, input().split())
A = [0] + list(map(int, input().split()))

# ボーナス部屋で増加する時間を記録したリスト
Bonus = [0] * (N + 1)
for _ in range(M):
    x, y = map(int, input().split())
    Bonus[x] = y

# 部屋に到達すると(i+1)番目で持ち時間が増加する
# ループ処理が終わったらYes
for i in range(1, N):
    if T <= A[i]:
        print("No")
        exit()
    T -= A[i]
    T += Bonus[i + 1]

print("Yes")
