N = int(input())

mountains = []

for i in range(N):
    S, T = map(str, input().split())
    intT = int(T)
    mountains.append([intT, S])

    # 先頭の要素が並び変わる
    mountains.sort(reverse=True)

    print(mountains[1][1])
