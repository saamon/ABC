k, n = map(int, input().split())
a = list(map(int, input().split()))
a.append(k + a[0])
# グラフとして考えて全体(K)から辺の最大値を引く
# 距離が負になるときの処理に気を付ける
# 池の基準点(0)を跨ぐときを考えてK+a[0]とする

max_distance = 0
for i in range(n):
    max_distance = max(max_distance, a[i + 1] - a[i])
print(k - max_distance)
