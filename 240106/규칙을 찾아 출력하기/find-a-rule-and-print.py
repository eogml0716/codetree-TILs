n = int(input())

for i in range(n):
    for j in range(n):
        if j >= i and i > 0 and j > 0 and i < n-1 and j < n-1:
            print(" ", end=" ")
        else: 
            print("*", end=" ")
    
    print()