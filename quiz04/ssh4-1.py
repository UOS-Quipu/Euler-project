import time

start =time.time()
def ispalindrome (num):
    string = str(num)
    length =len(string)
    for i in range(0,int(length/2)) :
        if string [i] != string[length -1-i] :
            return False
    return True

ans =0
for a in range (100, 999) :
    for b in range (100, 999) :
        c = a*b  
        if ispalindrome(c) :
            if c>ans :
                ans = c
            
print(ans)
print (time.time()-start,'s')

'''
906609
4.313871383666992 s
'''
