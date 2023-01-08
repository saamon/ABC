# abc256
# マスの状態を管理する(boolで判断)
# シミュレーション
N = int(input())
A = list(map(int, input().split()))

base = [False] * 4
point = 0

for i in A:
    base[0] = True
    next_base = [False] * 4
    for j in range(4):
        # Trueなら
        if base[j]:
            if j + i >= 4:
                point += 1
            else:
                # 足して4以下なら状態管理のリストを更新
                next_base[j + i] = True
    # baseをnext_baseに変更
    base = next_base
print(point)
