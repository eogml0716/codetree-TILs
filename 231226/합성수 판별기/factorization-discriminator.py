# 소수가 아니라면 나누어 떨어지는 수가 존재 해야한다.

n = int(input())

a = False

for i in range(1, n+1):
    if i % 2 == 0 or i % 3 == 0:
        a = True
    else:
        a = False

if a == True:
    print("C")
else:
    print("N")