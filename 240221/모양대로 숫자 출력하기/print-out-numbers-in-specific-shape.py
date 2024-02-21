n = int(input())

for i in range(n, 0, -1):
    for j in range(n):
        if (n-j < i+1):
            print(n - j, end=" ")
        else:
            print(" ", end=" ")
    print()