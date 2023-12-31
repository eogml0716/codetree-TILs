s = True
for i in range(1, 6):
    n = int(input())
    if n % 3 != 0:
        s = False
        break

if s == True:
    print(1)
else:
    print(0)