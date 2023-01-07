N = int(input())
T = list(map(int, input().split()))  # 問題かかる時間
M = int(input())

sumT = sum(T)

for i in range(M):
    p, x = map(int, input().split())
    print(sumT - (T[p - 1] - x))
