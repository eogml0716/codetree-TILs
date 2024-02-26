a, b = map(int, input().split())

count_val = 0
temp = 0
sum_val = 0
for i in range(a, b+1):
    temp = i
    while (i != 0):
        if (temp % i == 0):
            count_val += 1
        i -= 1
        
    if (count_val == 3):
        sum_val += 1
    count_val = 0
print(sum_val)