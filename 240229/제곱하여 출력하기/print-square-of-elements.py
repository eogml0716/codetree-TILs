n = int(input())

arr = list(map(int, input().split()))

arr2 = [arr[i] ** 2 for i in range(0, len(arr))]

for j in range(len(arr2)):
    print(arr2[j], end = " ")