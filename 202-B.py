S = input()
S = S[::-1]  # 反転

ans = ""  # 答えを格納

for x in S:
    if x == "0":
        ans += "0"  # 末尾へ追加する
    elif x == "1":
        ans += "1"
    elif x == "6":
        ans += "9"
    elif x == "8":
        ans += "8"
    elif x == "9":
        ans += "6"
print(ans)
