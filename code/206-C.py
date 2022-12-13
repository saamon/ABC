N = int(input())
A = list(map(int, input().split()))
from collections import Counter

ctr = Counter(A)
# 全体
ans = N * (N - 1) // 2
# 全体から等しいものを引く
for v in ctr.values():
    ans -= v * (v - 1) // 2
print(ans)
