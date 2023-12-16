sum = 0
cnt = 0

a, b = map(int, input().split())

for i in range(a, b+1):
    if (i % 5 == 0 or i % 7 == 0):
        sum += i
        cnt += 1
result = int(sum / cnt * 10) / 10
print(sum, result)