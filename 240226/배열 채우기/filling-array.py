arr = list(map(int, input().split()))

isTrue = False
for i in range(len(arr)):
    if(arr[i] == 0):
        isTrue = True
        for j in range(len(arr) - 2, -1, -1):
            print(arr[j], end = " ")
        break
    
if (len(arr) == 10 and isTrue == False):
    for j in range(len(arr) - 1, -1, -1):
            print(arr[j], end = " ")