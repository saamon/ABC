# abc260
# lambdaの使い方
# sorted([リストor辞書],key=lambda x:[keyにしたい要素])
n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = []
# 降順にソートする時はkeyにマイナスをつける
# 点数を元に降順にソートする
# リストaのソートしたものの番号リストを作成する
st = sorted([i for i in range(n)], key=lambda j: (-a[j], j))
# 上からxまでをansに入れる
ans += st[:x]
st = sorted(st[x:], key=lambda j: (-b[j], j))
ans += st[:y]
# y番目以降の配列をaとbの合計を元にソートする
st = sorted(st[y:], key=lambda j: (-a[j] - b[j], j))
ans += st[:z]

# ソートしたものを中身を確認しながら出力
for i in sorted(ans):
    print(i + 1)
