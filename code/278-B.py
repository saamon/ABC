H, M = map(int, input().split())
# 1分ずつ足して見間違えやすい時間になったら出力する
while True:
    A = H // 10
    B = H % 10
    C = M // 10
    D = M % 10
    h = 10 * A + C
    m = 10 * B + D
    if 0 <= h <= 23 and 0 <= m <= 59:
        print(H, M)
        exit()
    M += 1
    # 60分の時と、24時間の時の処理に注意
    if M == 60:
        M = 0
        H += 1
    if H == 24:
        H = 0
