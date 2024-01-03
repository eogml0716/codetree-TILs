n = int(input())

for i in range(n):
    if (i % 2 == 0):
        for j in range((i / 2) + 1):
            print("*", end=" ")
    else:
        for j in range(n-i+1):
            print("*", end=" ")
    print()

for i in range(n-2, -1, -1):
    if (i % 2 == 0):
        for j in range(i+1):
            print("*", end=" ")
    else:
        for j in range(n-i+1):
            print("*", end=" ")
    print()