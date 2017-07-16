check_num = 3
divide_num = 1
order = 1
import time
start = time.time()

while True:#order != 10001:
    for divide_num in range(2,check_num):
        if check_num % divide_num == 0:
            check_num = check_num+1
            
        elif divide_num == check_num-1:
            order = order+1
            check_num = check_num+1
            print("{0},{1}".format(order,check_num-1))

            if order == 10000:
                check_num = check_num-1
                print(check_num)
                total_time = time.time()-start
                print(total_time,"s")
                exit()


