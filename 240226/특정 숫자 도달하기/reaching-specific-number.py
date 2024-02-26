arr = list(map(int, input().split()))

sum_val = 0
average_val = 0
count_val = 0
for i in range(len(arr)):
    if (arr[i] >= 250):
        average_val = sum_val / count_val
        print(f"{sum_val} {average_val}")
        break
    else:
        sum_val += arr[i]
        count_val += 1