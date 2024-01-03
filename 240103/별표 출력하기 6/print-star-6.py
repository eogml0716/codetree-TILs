def print_symmetric_stars(n):
    # 상단 부분
    for i in range(n, 0, -1):
        print('  ' * (n - i) + '* ' * (2 * i - 1))

    # 하단 부분
    for i in range(2, n + 1):
        print('  ' * (n - i) + '* ' * (2 * i - 1))

# 예제로 n = 4를 사용하여 테스트
print_symmetric_stars(4)