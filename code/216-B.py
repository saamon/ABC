N = int(input())
L = [input().split() for i in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        if L[i] == L[j]:
            print("Yes")
            exit()
print("No")
