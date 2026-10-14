A,B,C  = map(int, input().split())

if (A <= B and A <= C):
    print(1, end=" ")
else:
    print(0, end=" ")

if (A == B and A == C and B == C):
    print(1)
else:
    print(0)
