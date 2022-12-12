N, W = map(int, input().split())

Cheese = []

for i in range(N):
    A, B = map(int, input().split())
    Cheese.append([A, B])

# 大きい順にソート
# 指定なしだと第一引数でソートする（美味しさ順）
Cheese.sort(reverse=True)

ans = 0

for i in range(N):
    Yammy = Cheese[i][0]
    Weight = Cheese[i][1]
    if Weight <= W:
        ans += Yammy * Weight
        W -= Weight
    else:
        # Wを超えてしまったら、残りのW*美味しさになる
        ans += W * Yammy
        break
print(ans)
