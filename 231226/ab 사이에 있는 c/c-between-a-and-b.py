a, b, c = map(int, input().split())

d = False

for i in range(a, b+1):
    if (i % c == 0):
        d = True
    
if d == True:
    print("YES")
else:
    print("NO")