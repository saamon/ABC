N = int(input())
T = input()

DX = [1, 0, -1, 0]
DY = [0, -1, 0, 1]

x, y = 0, 0
d = 0  # 現在の向き
for t in T:
    if t == "S":
        x += DX[d]
        y += DY[d]
    else:
        d = (d + 1) % 4  # 3の次は0なので4で割った余りを取る
print(x, y)
