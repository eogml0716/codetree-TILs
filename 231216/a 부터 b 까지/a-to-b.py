a, b = map(int, input().split())

while (b >= a):
    print(a, end = " ")
    if (a % 2 == 0):
        a += 3
    else:
        a *= 2