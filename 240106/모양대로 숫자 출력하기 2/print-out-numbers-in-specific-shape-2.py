cnt = 2
n = int(input())

for i in range(n):
    for j in range(n):
        print(cnt, end=" ")
        if (cnt == 8):
            cnt = 2
        else:
            cnt += 2
    print()