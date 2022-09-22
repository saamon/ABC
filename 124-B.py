n = int(input())
h = list(map(int, input().split()))

tmp = -1  # 一時的に値を保持する

ans = 0

for i in h:
    if i >= tmp:
        ans += 1
        tmp = i  # もし超えていたら入れ替える
print(ans)
