n=600851475143
i=100

while i*i<n:               # find sqrt n '=. i
    i+=1                   # you can use math.sqrt or numpy.sqrt
 
Eratosthenes=[1,1]+[0]*(i)
prime=[]

for x in range(2,i):          #I use sieveofEratosthenes to find primes
    if not Eratosthenes[x]:
        prime.append(x)
        for y in range(x,i,x):
            Eratosthenes[y]=1

print(prime[0:15]) #this code is to print primes to check it works well

count=0
ns_prime=[]

while n>1: #prime factorization by using list of primes before we found 
    while not n%prime[count]:
        ns_prime.append(prime[count]) 
        n/=prime[count]
    count+=1

print(ns_prime[-1]) #answer is ns_prime[-1] (6857) :)

''' If n had a prime which is greater than sqrt n(n^(1/2))
ex: 21 = 3 x 7(7 is greater than square root of 21), this solution
would not be work.
Luckily, n is not :) 
'''
