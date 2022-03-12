from sys import stdin, maxsize
from itertools import combinations

N = int(input())

def scan():
	return list(map(int, stdin.readline().split()))
	
arr = [scan() for i in range(N)]
ppl = set([i for i in range(N)])

c = combinations(ppl, len(ppl)//2)

ans = maxsize

for a in c:
	num1 = 0
	num2 = 0
	
	b = list(ppl-set(a))
	
	for i in range(len(a)):
		for j in range(len(a)):
			num1+=arr[a[i]][a[j]]
			num2+=arr[b[i]][b[j]]
			
	ans = min(ans, abs(num1-num2))
	
print(ans)
