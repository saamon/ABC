n, m, t = map(int, input().split())
battery = n  # 10
now = 0
for i in range(m):
    a, b = map(int, input().split())
    battery -= (a - now)
    if battery <= 0:
        print("No")
        exit()
    battery += (b - a)  # 休憩時に足す
    now = b
    battery = min(battery, n)

battery -= t - now
if battery <= 0:
    print("No")
else:
    print("Yes")
