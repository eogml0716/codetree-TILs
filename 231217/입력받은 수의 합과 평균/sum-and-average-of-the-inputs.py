sum_val = 0

n = int(input())

for i in range(1, n+1):
    a = int(input())

    sum_val += a

print(sum_val, round(sum_val/n, 1))