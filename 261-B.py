N = int(input())
# 二次元配列(表を作成する)
A = []

for i in range(N):
    S = input()
    listS = list(S)
    A.append(listS)  # 1文字ずつ格納される(リストに変換)

# i行目j列目にアクセス
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        if A[i][j] == "W" and A[i][j] != "L":
            print("incorrect")
            exit()  # 終了
        if A[i][j] == "L" and A[i][j] != "W":
            print("incorrect")
            exit()  # 終了
        if A[i][j] == "D" and A[i][j] != "D":
            print("incorrect")
            exit()  # 終了

# ここまで通せたら
print("correct")
