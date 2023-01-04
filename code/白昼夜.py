import re

# 正規表現
# re.subで文字列を置換できる
# (正規表現パターン、第二引数に置換先文字列、第三引数に処理対象)
s = input()
s = re.sub("eraser", "", s)
s = re.sub("erase", "", s)
s = re.sub("dreamer", "", s)
s = re.sub("dream", "", s)
print("YES" if len(s) == 0 else "NO")
