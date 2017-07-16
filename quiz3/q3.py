num = 600851475143
sp = 2
result = 0
while 1:
    if num % sp == 0:
        if sp > result:
            result = sp
        num = num / sp
        if num == 1:
            break
    else:
        sp = sp + 1
print(sp)
