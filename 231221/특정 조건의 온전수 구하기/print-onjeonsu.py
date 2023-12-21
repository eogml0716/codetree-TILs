n = int(input())

for i in range(1, n+1):
    if (i % 2 == 0) or (i % 10 == 5) or (i % 3 == 0 and i % 9 != 0):
        continue

    # 온전수 : 2로 나누어 떨어지면서, 일의 자리가 5가 아니면서, 3으로 나누어 떨어지지 않고 9로는 나누어떨어지는 수
    print(i, end=' ')