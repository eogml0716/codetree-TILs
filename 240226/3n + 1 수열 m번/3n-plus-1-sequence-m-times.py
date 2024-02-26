m = int(input())

count_val = 0
for i in range(m):
    n = int(input())

    while (n != 1):
        if (n % 2 ==0):
            n = n / 2
        else:
            n = 3 * n + 1
        count_val += 1
    print(count_val)

    count_val = 0