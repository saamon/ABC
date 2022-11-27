N = int(input())
X = list(map(int, input().split()))

# 集会を開く位置を0~100で全探索する
# ansで最小値を更新する
ans = float('inf')
for i in range(101):
    tmp = 0
    for x in X:
        tmp += (x - i) ** 2
    ans = min(ans, tmp)
print(ans)
