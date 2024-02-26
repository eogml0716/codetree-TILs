arr = list(map(int, input().split()))
cnt = 0

sum_val = 0
avg_val = 0

arr2 = []
for elem in range(len(arr)):
    if (arr[elem] == 0):
        break
    arr2.append(arr[elem])
    cnt += 1

print(sum(arr2), end = " ")

avg_val = sum(arr2) / cnt

print(f"{avg_val:.1f}")