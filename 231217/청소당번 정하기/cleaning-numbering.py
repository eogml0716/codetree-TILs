cnt2 = 0
cnt3 = 0
cnt12 = 0

n = int(input())

i = 1
for i in range(i, n+1):
    if (i % 2 == 0) and (i % 3 == 0) and (i % 12 == 0):
        cnt12 += 1
    elif (i % 2 == 0 and i % 3 == 0):
        cnt3 += 1
    elif (i % 2 == 0 and i % 12 == 0):
        cnt12 += 1
    elif (i % 3 == 0 and i % 12 == 0):
        cnt12 += 1
    elif (i % 12 == 0):
        cnt12 += 1
    elif (i % 3 == 0):
        cnt3 += 1
    elif (i % 2 == 0):
        cnt2 += 1

print(cnt2, cnt3, cnt12)