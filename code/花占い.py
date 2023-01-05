n = int(input())
A = list(map(int, input().split()))
# 3で割った時の余りが2
# 2で割った時の余りが0
# 3と2の最小公倍数の6（周期）で判断
# どちらも好きor大好きの1,3に合わせる
ans = 0
for i in A:
    b = i % 6
    if b == 2 or b == 4:
        ans += 1
    elif b == 5:
        ans += 2
    elif b == 0:
        ans += 3
print(ans)
