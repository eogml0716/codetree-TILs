count = 3
while True:
    n = int(input())

    if n % 2 == 0:
        value = n // 2
        print(value)
        count = count - 1
    else:
        count = count - 1
    
    if count == 0:
        break