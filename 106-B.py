N = int(input())
ans = 0
for n in range(1, N + 1, 2):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
        if cnt == 8:
            ans += 1
print(ans)  # cntはfor文中での使用のためスコープに気をつける
