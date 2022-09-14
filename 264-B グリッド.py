# R行目とC列目->2次元配列
R, C = map(int, input().split())
# マス目を作る(0も含む)
# 2次元配列(16 * 16 のグリッドを生成する)
Grid = [[0] * 16 for i in range(16)]

# 1が黒で0が白
for i in range(1, 16):
    Grid[1][i] = 1
    Grid[i][1] = 1
    Grid[15][i] = 1
    Grid[i][15] = 1
for i in range(3, 14):
    Grid[3][i] = 1
    Grid[i][3] = 1
    Grid[13][i] = 1
    Grid[i][13] = 1
for i in range(5, 12):
    Grid[5][i] = 1
    Grid[11][i] = 1
    Grid[i][5] = 1
    Grid[i][11] = 1
for i in range(7, 10):
    Grid[7][i] = 1
    Grid[i][7] = 1
    Grid[11][i] = 1
    Grid[i][11] = 1

if Grid[R][C] == 1:
    print("black")
else:
    print("white")
