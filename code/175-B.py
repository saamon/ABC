n = int(input())
l = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # 比較演算子（!=）を使う時は注意！
            # 全ての組み合わせが評価される訳ではない
            if l[i] != l[j] and l[j] != l[k] and l[i] != l[k]:
                if l[i] < l[j] + l[k] and l[j] < l[i] + l[k] and l[k] < l[i] + l[j]:
                    cnt += 1
print(cnt)
