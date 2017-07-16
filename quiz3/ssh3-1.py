import time

start =time.time()
n=600851475143
i=2

while i*i <n :
    while n%i==0:
        n=n/i
    i=i+1

print (n)
print(time.time()-start,'s')

'''
6857.0
0.004001617431640625 s
'''
