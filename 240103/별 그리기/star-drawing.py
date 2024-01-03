n = int(input())

# 윗쪽 별표 출력
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range((2 * i) + 1):
        print("*", end="")
    print()

# 아랫쪽 별표 출력
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range((2 * i) + 1):
        print("*", end="")
    print()