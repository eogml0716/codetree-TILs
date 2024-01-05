cnt = 9
n = int(input())

for i in range(n):
    for j in range(n):
        print(cnt, end="")
        if (cnt == 1):
            cnt = 9
        else:
            cnt -= 1
    print()