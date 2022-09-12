N = int(input())
A = list(map(int, input().split()))
A.sort()
B = list(range(1, N + 1))  # 1からNまでのリストを生成

print("Yes" if A == B else "No")
