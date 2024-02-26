n = int(input())

sum_val = 0
for i in range(n):
    a, b = map(int, input().split())

    for j in range(a, b+1):
        if (j % 2 ==0):
            sum_val += j
    
    print(sum_val)
    sum_val = 0