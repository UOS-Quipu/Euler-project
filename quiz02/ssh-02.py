import time
start =time.time()
def fibo():
    array = [1,2]
    sum1=0
    index =1
    while (array[index]<4000000):
        array.append(array[index]+array[index-1])
        index = index+1

    i=0
    for i in range(0, index) :
        if array[i]%2 ==0 :
            sum1 += array[i];
            
    print (sum1);
fibo()
print(time.time()-start,'s')

'''실행 결과
4613732
0.0 s
'''
