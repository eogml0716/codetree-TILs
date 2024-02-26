arr = list(map(int, input().split()))

for i in range(len(arr)):
    if(arr[i] == 0):
        for j in range(len(arr) - 2, -1, -1):
            print(arr[j], end = " ")
    
if (len(arr) == 10):
    for j in range(len(arr) - 1, -1, -1):
            print(arr[j], end = " ")