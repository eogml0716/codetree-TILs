n = int(input())
arr = list(map(float, input().split()))

sum_val = 0
average_val = 0
for i in range(n):
    sum_val += arr[i]

average_val = sum_val / n

print(f"{average_val:.1f}")

if (average_val >= 4.0):
    print("Perfect")
elif (average_val >= 3.0):
    print("Good")
else:
    print("Poor")