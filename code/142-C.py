N = int(input())
A = list(map(int, input().split()))
# Aを辞書型で受け取る
A = {i: A[i] for i in range(N)}
# 値をキーにしてソート
A = sorted(A.items(), key=lambda x: x[1])
# キーを取り出す
A = [a[0] for a in A]
# 1indexにする
A = [a + 1 for a in A]
print(*A)
