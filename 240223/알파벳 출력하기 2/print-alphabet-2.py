n = int(input())

cnt = 65

for i in range(n):
    for j in range(n):
        if (j < i):
            print(" ", end=" ")
        else:
            print(chr(cnt), end=" ")
            cnt += 1

        if (cnt == 91):
            cnt = 65
    print()