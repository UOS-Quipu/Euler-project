a = 340
while a<1000 :
    a = a + 1
    b = 340
    while b<1000:
        b = b+1
        c = str(a * b)
        if c[0]==c[5] and c[1]==c[4] and c[2]==c[3]:
            print (c)
            pass
