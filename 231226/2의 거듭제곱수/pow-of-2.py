n = int(input())
x = 0

while True: 
    if (n == 1):
        print(x)
        break
    
    n //= 2
    x += 1