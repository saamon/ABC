import math

A, B, W = map(int, input().split())
C = math.floor(1000 * W / A)
D = math.ceil(1000 * W / B)

if D > C:
    print("UNSATISFIABLE")
else:
    print(min(C, D), max(C, D))
