n = int(input())
A = [input() for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if A[i][j] == "W":
            if A[j][i] != "L":
                print("incorrect")
                exit()
        elif A[i][j] == "D":
            if A[i][j] != "D":
                print("incorrect")
                exit()
        elif A[i][j] == "L":
            if A[j][i] != "W":
                print("incorrect")
                exit()
print("correct")
