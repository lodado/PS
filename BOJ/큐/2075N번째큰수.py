import sys
import heapq

def scanInt():
	return map(int, sys.stdin.readline().split())

[N] = list(scanInt())


heapArr = []

def push(heap):
	for j in scanNow:
		heapq.heappush(heap, j)

for i in range(N):
	scanNow = list(scanInt())
	push(heapArr)

	if(i>=1):
		for j in range(N):
			heapq.heappop(heapArr)
		

print(heapArr[0])
