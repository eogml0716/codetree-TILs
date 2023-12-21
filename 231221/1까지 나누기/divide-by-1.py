n = int(input())
i = 1
val = n  # 초기 값은 n으로 설정

while True:
    val = val // i  # 이전 나눗셈 결과를 다음 단계에서 사용
    if val <= 1:
        print(i)  # 여기서 i를 출력 (i-1이 아님)
        break
    i += 1