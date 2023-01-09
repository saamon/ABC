from itertools import groupby

s = input()
res = ""

for key, val in groupby(s):
    res += key
    # グループがitertoolsのオブジェクトとして返されるので、
    # 扱いやすいリストに変換するのが一般的
    # リストの長さを返すようにする
    res += str(len(list(val)))

print(res)
