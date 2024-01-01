# 정수 n의 값을 입력받아 
n = int(input())

# 별표를 출력하는 프로그램을 아래 예를 참고하여 작성해보세요.
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()