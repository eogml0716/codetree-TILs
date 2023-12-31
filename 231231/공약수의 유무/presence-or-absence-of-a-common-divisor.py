def gcd(x, y):
    # y가 0이 될 때까지 반복
    while y:
        x, y = y, x % y
    return x

def find_common_divisors(a, b, num1, num2):
    # 두 수의 최대공약수를 찾음
    common_gcd = gcd(num1, num2)

    # 최대공약수의 약수 중 a와 b 사이에 있는지 확인
    for i in range(a, min(b, common_gcd) + 1):
        if common_gcd % i == 0:
            return 1  # 공약수가 존재함
    return 0  # 공약수가 존재하지 않음

# 예제 입력에 대한 결과를 확인
a, b = map(int, input().split())
result = find_common_divisors(a, b, 1920, 2880)
print(result)