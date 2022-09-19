from collections import Counter

N, M = map(int, input().split())
cnt = Counter()  # Counter(全ての出現回数を記録する)
for _ in range(N):
    # リストが1から始まる
    a = list(map(int, input().split()))[1:]
    cnt += Counter(a)  # aのリストの出現回数を記録する
ans = 0
for i in cnt.values():
    if i == N:  # 数え上げた要素数が一致していたら
        ans += 1
print(ans)
