i=int(1<<20) # i=2^20 

Eratosthenes=[1,1]+[0]*(i)
prime=[1]

for x in range(2,i):          #I use sieve of Eratosthenes to find primes
    if not Eratosthenes[x]:
        prime.append(x)
        for y in range(x,i,x):
            Eratosthenes[y]=1

print(prime[10001]) #this code is to print 10001th prime(104743) :)

