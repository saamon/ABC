N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans1 = 0
ans2 = 0

# 数が一緒かをif文
# そこから分岐する
# i,j がindex
for i, a in enumerate(A):
    for j, b in enumerate(B):
        if a == b:
            if i == j:  # 位置と数値が一緒
                ans1 += 1
            else:
                ans2 += 1
print(ans1)
print(ans2)
