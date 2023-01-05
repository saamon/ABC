H, W = map(int, input().split())
C = [input().split() for _ in range(H)]
# print(C)
for i in range(H):
    print(*C[i] * 2)
