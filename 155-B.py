n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if a[i] % 2 == 0:
        ans = a[i]
    if ans % 3 != 0 and ans % 5 != 0:
        print("DENIED")
        exit()
print("APPROVED")
