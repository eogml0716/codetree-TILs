arr = list(map(int, input().split()))

f_arr1_sum_value = sum(arr[::2])
f_arr2_sum_value = sum(arr[1::2])

if f_arr1_sum_value > f_arr2_sum_value:
    print(f_arr1_sum_value - f_arr2_sum_value)
else: 
    print(f_arr2_sum_value - f_arr1_sum_value)