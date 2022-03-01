from sys import stdin
from collections import deque, defaultdict

def scan():
	return list(map(int, stdin.readline().split()))
	
[n, d, k, c] = scan()

arr = []

for i in range(n):
	[sc] = scan()
	arr.append(sc)

arr = arr + arr
left, right = 0, 0
sums = defaultdict(int)
sums[c]+=1
ans = 0

while(left<n):
	if(right>=k):
		ans = max(ans, len(sums))
		sums[arr[left]]-=1
		if(sums[arr[left]]==0):
			del sums[arr[left]]
		left+=1
	sums[arr[right]]+=1
	right+=1
print(ans)
