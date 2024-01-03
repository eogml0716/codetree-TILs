n = int(input())

for i in range(n):
    if (i % 2 == 0):
        for j in range(int(i / 2) + 1):
            print("*", end=" ")
    else:
        for j in range(n-int((i-1)/2)):
            print("*", end=" ")
    print()

for i in range(n-1, -1, -1):
    if (i % 2 == 0):
        for j in range(int(i / 2) + 1):
            print("*", end=" ")
    else:
        for j in range(n-int((i-1)/2)):
            print("*", end=" ")
    print()