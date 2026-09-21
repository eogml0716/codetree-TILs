a, b, c = 5, 6, 7

tempA = a
tempB = b
tempC = c
b = tempA
c = tempB
a = tempC 
 
print(f"{a}")
print(f"{b}")
print(f"{c}")