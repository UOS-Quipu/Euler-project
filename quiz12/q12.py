import math
i = 0
result = 0

def count(n):
    s=[]
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            s.append(i)
            s.append(int(n / i))
    return len(s)

while count(result) < 500:
    i = i+1
    result = result+i
print(result)
