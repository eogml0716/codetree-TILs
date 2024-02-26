a, b = map(int, input().split())

sum_val = 0
temp = 0
count_val = 0
# 약수를 일단 어떻게 구하지?
for i in range(a, b+1):
    temp = i
    while (i != 0):
        if (temp % i == 0 and temp != i):
            sum_val += i
        i -= 1
    
    if (sum_val == temp):
        count_val += 1
    # 왤캐 초기화를 안하지?
    sum_val = 0

print(count_val)