import time

start=time.time()
a=1
sum1 =0
while a <999 :
    a = a+1
    if a%3==0 or a%5 ==0 :
        sum1 = sum1+a
#        print (a)
        
print (sum1)

total_time=time.time()-start

print(total_time,"s")
