arr = list(map(int, input().split()))

f_arr2 = arr[1::2]
# print(f_arr2)
f_arr3 = arr[2::3]

sum_value2 = sum(f_arr2)
avg_value3 = sum(f_arr3) / len(f_arr3)

print(f"{sum_value2} {avg_value3:.1f}")