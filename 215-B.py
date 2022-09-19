# 入力の受け取り
N = int(input())

# k=0~999まで
for k in range(1000):
    # もしN<2^kならば
    if N < 2 ** k:
        # 一つ前のkが答え
        print(k - 1)
        # 終了
        exit()
