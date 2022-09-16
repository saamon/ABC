N = int(input())
S = input()
ans = ""
for i in range(len(S)):
    x = ord(S[i]) - 65
    a = (x + N) % 26 + 65
    ans += chr(a)
print(ans)
