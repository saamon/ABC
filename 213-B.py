N = int(input())
A = list(map(int, input().split()))
ans = []

for i in range(N):
    ans.append((A[i], i + 1))  # スコアでソートする
    ans.sort()

print(ans[-2][1])  # -2番目+選手番号のインデックス[0,1]
