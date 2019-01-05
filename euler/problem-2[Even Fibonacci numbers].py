def func():             #function to solve
    a,b,c=1,1,0         # f(n)=c, f(n-1)=b and f(n-2)=a
    while c<4000000:
        c=a+b           # fibo(n)=fibo(n-1)+fibo(n-2)
        if not c%2:
            yield c     # yield even fibonacci numbers
        a,b=b,c         # below four million
        
print(sum(func()))      #print sum(4613732) :)
