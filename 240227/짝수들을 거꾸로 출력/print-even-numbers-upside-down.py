# TODO: 해설처럼 풀어보도록 노력하자

n = int(input())  # 입력받을 숫자의 개수
arr = list(map(int, input().split()))  # n개의 정수를 한 줄에 입력받아 리스트로 변환

arr2 = []  # 짝수를 저장할 새로운 리스트
for num in arr:  # arr 리스트의 각 원소에 대해
    if num % 2 == 0:  # 원소가 짝수인지 확인
        arr2.append(num)  # 짝수이면 arr2에 추가

# arr2에 저장된 짝수들을 역순으로 출력
for i in range(len(arr2) - 1, -1, -1):  # arr2의 마지막 인덱스부터 0까지 역순으로 순회
    print(arr2[i], end=" ")  # 공백을 사이에 두고 짝수들을 출력