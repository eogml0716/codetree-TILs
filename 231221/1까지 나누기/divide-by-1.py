n = int(input())
i = 1
val = n  # 초기 값은 n으로 설정

while True:
    if val <= 1:
        print(i - 1)  # 나눗셈이 진행된 횟수는 i - 1
        break
    val = n // i  # 여기에서 나눗셈을 진행
    i += 1