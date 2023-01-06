# A:料理 B:満足度 C:追加の満足度
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = sum(B)
for i in range(N - 1):
    # 料理iを食べた直後に料理i+1を食べると満足度Ciを追加
    # rangeの範囲は-1
    # 1indexで書かれているので0indexに直す
    if A[i] + 1 == A[i + 1]:
        ans += C[A[i] - 1]
print(ans)
