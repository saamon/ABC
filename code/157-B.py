aaa = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
for _ in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if aaa[j][k] == b:
                aaa[j][k] = 0  # bがあったら0にする

ans = 'No'
for i in range(3):
    if aaa[i][0] == aaa[i][1] == aaa[i][2] == 0:
        ans = 'Yes'
    if aaa[0][i] == aaa[1][i] == aaa[2][i] == 0:
        ans = 'Yes'
if aaa[0][0] == aaa[1][1] == aaa[2][2] == 0:
    ans = 'Yes'
if aaa[2][0] == aaa[1][1] == aaa[0][2] == 0:
    ans = 'Yes'
print(ans)
