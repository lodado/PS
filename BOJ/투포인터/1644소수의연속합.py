import math

N = int(input())

end = N+1

arr = [True for _ in range(end)]
prime = []

for i in range(2, end):
	if(arr[i]):
		prime.append(i)
		for j in range(2*i, end, i):
			arr[j] = False

length = len(prime)
sums = 0
ans = 0
left = 0

for i in range(length):
	
	sums+=prime[i]
	while(sums>N):
		sums-=prime[left]
		left+=1
	
	if(sums==N):
		ans+=1

print(ans)
