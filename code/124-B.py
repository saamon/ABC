n = int(input())
h = list(map(int, input().split()))

tmp_max = -1
count = 0

# 前よりも高ければ値を更新する
for i in range(n):
    if h[i] >= tmp_max:
        count += 1
        tmp_max = h[i]
print(count)
