import math

N, M = map(int, input().split())
maxi = 1000001

check = [1 for i in range(M-N+1)]
i=2
cnt=0

while(i*i<=M):
	start = N//(i*i)
	
	if(start*i*i!=N):
		start+=1
	
	while(start*i*i<=M):
		check[start*i*i-N] = 0
		start+=1
	i+=1
	
print(check.count(1))
	
