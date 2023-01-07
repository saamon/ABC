S = input()
ans = []

for k in range(0, len(S)):
    # 先頭除く最後まで
    # 先頭までをそれぞれスライスで取り出し結合する
    ans.append(S[k:len(S)] + S[0:k])
print(min(ans))
print(max(ans))
