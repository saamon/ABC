N = int(input())
S = [input() for _ in range(N)]

# zip:転置
# "".join(s) ->リストの要素を結合する
for s in zip(*S):
    print("".join(s)[::-1])
