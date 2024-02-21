n = int(input())

cnt = 1

for i in range(n, 0, -1): # 첫번째 for문이 행을 의미하고
    for j in range(1, n+1): # 두번째 줄이 열을 의미하며, 공백이 있더라도 이거 코딩테스트식 눈속임 인 거 알았다면 쉽게 풀었으려나?
        if j <= n-i:  
            print(" ", end=" ")
        else:
            print(cnt, end=" ")  
            cnt += 1
            if cnt == 10: 
                cnt = 1
    print()