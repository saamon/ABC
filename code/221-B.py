S = input()
T = input()

if S == T:
    print("Yes")
    exit()

# 文字列のままだと変更できないのでリストに変換する
listS = list(S)
listT = list(T)

for i in range(len(S) - 1):
    # i文字目,i+1文字目とi+1文字目,i文字目を交換
    listS[i], listS[i + 1] = listS[i + 1], listS[i]
    if listS == listT:
        print("Yes")
        exit()
    # 元に戻す
    listS[i], listS[i + 1] = listS[i + 1], listS[i]
print("No")
