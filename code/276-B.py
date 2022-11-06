N, M = map(int, input().split())
# 頂点数Nのグラフを定義する
# 1index
G = [[] for i in range(N + 1)]
# M本の辺を受け取る
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b)
    G[b - 1].append(a)
# print(G)
for i in range(N):
    G[i].sort()
    print(len(G[i]), *G[i])
