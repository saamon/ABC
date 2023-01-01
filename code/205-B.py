n = int(input())
a = list(map(int, input().split()))
a.sort()
a2 = []

ans = "No"
for i in range(1, n + 1):
    a2.append(i)
    if a == a2:
        ans = "Yes"
print(ans)
