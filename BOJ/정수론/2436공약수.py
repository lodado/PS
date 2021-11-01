import math
import sys

N, M = map(int, input().split())

def GCD(r1, r2):
	return GCD(r2, r1%r2) if r2 !=0 else r1
	
num = ((M)//N)

ab = math.ceil(math.sqrt(num))

mini = sys.maxsize+1
sva = 1
svb = 1

for i in range(1, ab+1):
	
	if(num%i==0):
		a = num//i * N
		b = i * N
		
		if(mini>a+b and GCD(a,b)==N):
			mini=a+b
			sva = a
			svb = b

print(svb, sva)
		
		

