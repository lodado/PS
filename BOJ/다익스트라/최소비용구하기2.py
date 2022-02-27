from sys import stdin, maxsize
import heapq

def scan():
	return list(map(int, stdin.readline().split()))
	
N = int(input())
M = int(input())

nodes = [[] for i in range(N+1)]
dist = [[maxsize, -1] for _ in range(N+1)]

for i in range(M):
	[start, end, value] = scan()
	nodes[start].append([end, value])

[startPoint, endPoint] = scan()	

hq = []
heapq.heappush(hq, [0, startPoint])
dist[startPoint] = [0, -1]

while(hq):
	cost, now = heapq.heappop(hq)
	if(cost>dist[now][0]):
		continue
	
	for [end, endCost] in nodes[now]:
		newCost = cost + endCost
		if(dist[end][0]>newCost):
			dist[end][0]= newCost
			dist[end][1] = now
			heapq.heappush(hq, [newCost, end])

index = dist[endPoint][1]
ans = [endPoint]

while(index!=-1):
	ans.append(index)
	index = dist[index][1]

print(dist[endPoint][0])
print(len(ans))
print(*ans[::-1])
