n = int(input())
x = 0

while True: 
    if (n == 0):
        print(x-1)
        break
    
    n //= 2
    x += 1