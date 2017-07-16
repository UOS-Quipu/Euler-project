import time

start =time.time()
a=1
b=2
c=3 
sum1 =0

while c <4000000 :
    c= a+b
    a=b
    b=c
    if c%2==0 : 
        sum1 += c


sum1 += 2    
print (sum1)
print(time.time()-start,'s')

'''실행 결과
4613732
0.0 s'''
