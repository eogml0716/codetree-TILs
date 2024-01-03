def print_symmetric_stars(n):
    # 상단 부분
    for i in range(n, 0, -1):
        print('  ' * (n - i) + '* ' * (2 * i - 1))

    # 하단 부분
    for i in range(2, n + 1):
        print('  ' * (n - i) + '* ' * (2 * i - 1))

n = int(input())
print_symmetric_stars(n)