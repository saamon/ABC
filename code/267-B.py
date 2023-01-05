# 0:倒れている,1:立っている
s = list(input())

if s[0] == '1':
    print("No")
    exit()

# 行確認用の配列
col = [False] * 7
col[0] = s[6] == '0'
col[1] = s[3] == '0'
col[2] = s[1] == '0' and s[7] == '0'
col[3] = s[0] == '0' and s[4] == '0'
col[4] = s[2] == '0' and s[8] == '0'
col[5] = s[5] == '0'
col[6] = s[9] == '0'
ans = False

for i in range(7):
    for j in range(i + 1, 7):
        for k in range(i + 2, 7):
            if not (i < j < k):
                continue
            if col[i] == False and col[k] == False and col[j] == True:
                ans = True

print('Yes') if ans else print('No')
