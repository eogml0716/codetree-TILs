# 해설처럼 풀어보려고 노력하자 
arr = list(map(int, input().split()))

isTrue = False
for i in range(len(arr)):
    if(arr[i] == 0):
        isTrue = True
        for j in range(i - 1, -1, -1):
            print(arr[j], end = " ")
        break
    
if (len(arr) == 10 and isTrue == False):
    for j in range(len(arr) - 1, -1, -1):
            print(arr[j], end = " ")