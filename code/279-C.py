H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

from collections import Counter

cs = Counter()
for col in zip(*S):
    s = ''.join(col)
    # Sの各列の文字列をカウント
    cs[s] += 1

ts = Counter()
for col in zip(*T):
    s = ''.join(col)
    # Tの各列の文字列をカウント
    ts[s] += 1

# Sの各列の文字列とTの各列の文字列が一致するか
print('Yes' if cs == ts else 'No')
