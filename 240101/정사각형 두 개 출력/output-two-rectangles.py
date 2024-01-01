#정수 n이 주어졌을 때,
n = int(input())

# n x n 크기의 정사각형을 두 개 출력합니다.
# **
# **

# **
# **

# 일단 정사각형 1개를 출력 해보자

for _ in range(2):
    for _ in range(n):
        for _ in range(n):
            print("*", end="")
        print()
    print()