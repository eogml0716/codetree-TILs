n = int(input())
cnt= n
# 이게 계단식으로 출력이 되든 그렇지 않든 뭐라고 해야되지, 그냥 아예 정사각형 판이라고 생각하는 게 마음 편할듯?
for i in range(1, n+1):
    for j in range(1, i+1):
        print(cnt-i+j, end=" ")
    print()