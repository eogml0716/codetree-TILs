# 그냥 한번에 딱 맞추는 방법에 대해서는 고려를 못하니?
n = int(input())

for i in range(n, 0, -1):
    for j in range(1, i+1):
        if (i == j):
             print(f"{n-i+1} * {j} = {(n-i+1) * j}", end="")
        else:
            print(f"{n-i+1} * {j} = {(n-i+1) * j}", end = " / ")
    print()