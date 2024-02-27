arr = list(map(int, input().split()))

# 0이 나오는 인덱스에서 -1, -2, -3에 해당하는 인덱스의 값을 다 더해주면 되겠다.

sum_value = 0

for i in range(len(arr)):
    if(arr[i] == 0):
        sum_value = arr[i-1] + arr[i-2] + arr[i-3]
        break

print(sum_value)