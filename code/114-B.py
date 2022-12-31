s = input()
ans = 10000
for i in range(len(s) - 2):  # 3つ取り出すので端2つはできない
    ans = min(ans, abs(int(s[i:i + 3]) - 753))  # i ~ i+2 まで
print(ans)
