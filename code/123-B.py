# 10の倍数との差が最大のものを合計時間から引けば良い
# 10の倍数との差が最大-> 一番待ち時間が多い
# 最後は10の倍数に変換しないので差が最大を選ぶ
import math

A = [int(input()) for i in range(5)]
ans = 0
diff = 0

for i in A:
    ans += math.ceil(i / 10) * 10
    diff = max((math.ceil(i / 10) * 10) - i, diff)
print(ans - diff)
