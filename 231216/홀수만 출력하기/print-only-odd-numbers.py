n = int(input())

for _ in range(n):
    m = int(input())

    if m % 2 != 0 and m % 3 == 0:
        print(m)