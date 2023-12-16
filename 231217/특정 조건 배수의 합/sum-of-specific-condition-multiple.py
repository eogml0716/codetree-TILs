sum_val = 0

a, b = map(int, input().split())

big = 0
small = 0
if (a >= b):
    big = a
    small = b
else:
    big = b
    small = a
    
for i in range(small, big+1):
    if (i % 5 == 0):
        sum_val += i

print(sum_val)