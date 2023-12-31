a, b, c = map(int, input().split())
s = False

for i in range(a, b+1):
    if c % i == 0:
        s = True

if s == False:
    print("NO")
else:
    print("YES")