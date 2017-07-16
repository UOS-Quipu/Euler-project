import math
for a in range(0, 500):
    for b in range(0, 500):
        pita2 = (a*a)+(b*b)
        pita = math.sqrt(pita2)
        hap = pita + a + b
        if hap == 1000:
            result = a * b * pita
print(result)
