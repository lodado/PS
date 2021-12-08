import sys 
import heapq

def scan():
	return sys.stdin.readline()
	
def scanList():
	return map(int, scan().split())

class Node:
	def __init__(self, number):
		self.number = number
		self.next = []
		self.value = None
	
	def append(self, next, value):
		self.next.append([next, value])
	
N, E = scanList()

nodes = [Node(i) for i in range(N+1)]

def dijk(start, end):
	global nodes
	global N
	
	dist = [987654321 for i in range(N+1)]
	dist[start] = 0
	
	hq = [[0, start]]
	
	while(hq):
		
		cost, nowPoint = heapq.heappop(hq)
		if(cost> dist[nowPoint]):
			continue
		
		for nextPoint, value in nodes[nowPoint].next:
			if(cost+value<dist[nextPoint]):
				dist[nextPoint] = cost + value
				heapq.heappush(hq, [cost+value, nextPoint])

	return dist[end]
	
for i in range(E):
	first, second, value = scanList()
	
	nodes[first].append(second, value)
	nodes[second].append(first, value)

v1, v2 = scanList()

first = dijk(1, v1)+dijk(v1, v2)+dijk(v2, N)
second = dijk(1, v2)+dijk(v2, v1)+dijk(v1, N)

if(first>=987654321 and second>=987654321):
	print(-1)
else:
	print(min(first, second))
