arr = list(map(float, input().split()))

sum_val = 0
average_val = 0
for i in range(len(arr)):
    sum_val += arr[i]

average_val = sum_val / 8

print(f"{average_val:.1f}")