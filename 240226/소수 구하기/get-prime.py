n = int(input())

temp = 0
count_val = 0
# 약수가 2개인 문제를 찾는 거 잖아? 그리고 end = " "로 마무리 하면 될 거 같은데
for i in range(1, n+1):
    temp = i
    while(i != 0):
        if (temp % i == 0):
            count_val += 1
        i -= 1
    if (count_val == 2):
        print(temp, end= " ")
    count_val = 0