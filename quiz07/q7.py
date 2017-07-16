import math
num = 4
i = 10
while 1:
    i = i + 1
    pas = True
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            pas = False
            break
    if pas:
        num = num + 1
    if num == 10001:
        print(i)
        break
