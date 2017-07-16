import math
result = 0
def pri(n):
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f+2) == 0:
            return False
        f = f + 6
    return True
for i in range(2, 2000000):
    if pri(i):
        result = result + i
print(result)
