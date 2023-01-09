low, high = map(int, input().split())
N = int(input())
A = [int(input()) for i in range(N)]

for a in A:
    if a < low:
        print(low - a)
    elif low <= a <= high:
        print(0)
    elif high < a:
        print(-1)
