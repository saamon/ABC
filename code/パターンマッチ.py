from itertools import product
from re import search

# re search:一致する箇所が一つでもあればok
# itertools product:AとBの直積を返す
# >>> A = ('a', 'b', 'c')
# >>> B = ('d', 'e')
# >>> list(itertools.product(A, B))
# [('a', 'd'), ('a', 'e'), ('b', 'd'), ('b', 'e'), ('c', 'd'), ('c', 'e')]
S = input()

cs = set(S)
cs.add('.')

result = 0
for i in range(1, 4):
    for p in product(cs, repeat=i):
        if search(''.join(p), S):
            result += 1
print(result)
