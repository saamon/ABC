s = input()
s1 = len(s)
# 文字列同士の足し算なのでlenは使えない(strに変換)
print(s[0] + str(s1 - 2) + s[-1])
