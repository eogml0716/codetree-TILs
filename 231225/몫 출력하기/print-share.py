count = 3

while True:
    try:
        n = int(input())

        if n % 2 == 0:
            value = n // 2
            print(value)
            count -= 1

            if count == 0:
                break

    except EOFError:
        break