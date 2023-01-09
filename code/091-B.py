# N:Blue,M:Red
# Blue:Plus Red:Minus
import collections

CC = collections.Counter()
N = int(input())
for i in range(N):
    CC[input()] += 1
M = int(input())
for i in range(M):
    CC[input()] -= 1

ans = 0
for k, v in CC.items():
    ans = max(ans, v)
    # print(k, v)
print(ans)
