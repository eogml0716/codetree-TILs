arr = list(map(int, input().split()))

arr2 = []

cnt = 0
# sum_val = 0

for elem in range(len(arr)):
    if (arr[elem] == 0):
        break
    if(arr[elem] % 2 == 0):
        arr2.append(arr[elem])
        cnt += 1

print(cnt, end=" ")
print(sum(arr2))