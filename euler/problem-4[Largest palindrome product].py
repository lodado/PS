result=int(0)

for i in range(100,1000):               # use brute-force to find result
    for j in range(100,1000):
        st = str(i*j)           #string st = i * j
        check=bool(True)        #boolen for check!

        for x in range(0,len(st)):
            if st[x] != st[len(st)-(x+1)]: #is it palindrome or not?
                check=False                #unless it is,than pass
                break
        if check:                          #if it is, than check maximum or not 
            result=max(result,int(st))

print(result) # print result(906609) :)
