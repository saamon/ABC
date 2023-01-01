N = int(input())
S = input()
res = 0
for i in range(N):
    SetA = set(S[i:])
    SetB = set(S[:i])
    res = max(res, len(SetA & SetB))
print(res)
