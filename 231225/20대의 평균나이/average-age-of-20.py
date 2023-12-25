count = 0
sum_value = 0

while True:
    n = int(input())

    if n // 10 != 2:
        average = sum_value / count
        print(f"{average:.2f}")
        break
    else:
        sum_value += n    
        count += 1