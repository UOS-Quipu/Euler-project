import time

start =time.time()

target = 600851475143
i=2
result =[2,3]

def checkprime(n):
    if(n%2==0 or n%3 is 0) :
        return False
    else :
        return True
    
while (i<=target) :
    if(target%i ==0) :
        if(checkprime(i) is True) :
            target = target/i
            result.append(i)
    i=i+1
        
print (result)
result.sort
print(result)
result.reverse()
print(result)

print(time.time()-start,'s')

'''
[2, 3, 71, 839, 1471, 6857]
[2, 3, 71, 839, 1471, 6857]
[6857, 1471, 839, 71, 3, 2]
0.006002902984619141 s

'''
