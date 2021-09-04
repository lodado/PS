import sys
import itertools
from collections import deque

M, N, K = map(int, (sys.stdin.readline().split()))

flag = [[False for i in range(N)] for j in range(M)]
lists = [[0 for i in range(N)] for j in range(M)]

dx = [0, 0, 1, -1]
dy = [1, -1,0, 0]

def bfs(x, y, tag):
	global flag, lists 
	
	if (flag[y][x]):
		return
	
	arr = deque([[lists[y][x], x , y]])

	while (arr):
		
		first, nowX, nowY = arr.popleft()
		
		if(flag[nowY][nowX] == True):
			continue
		
		flag[nowY][nowX] = True
		lists[nowY][nowX] = tag
		
		for i in range(4):
			if(0<=nowX+dx[i]<N and 0<=nowY+dy[i]<M and flag[nowY+dy[i]][nowX+dx[i]]==False):
				arr.append([lists[nowY+dy[i]][nowX+dx[i]], nowX+dx[i], nowY+dy[i]])

		
for i in range(int(K)):
	x1, y1, x2, y2 = map(int, (sys.stdin.readline().split()))
	
	startX = x1 if x1<x2  else x2
	startY = y1 if y1<y2 else y2
	
	Y = abs(y1 - y2)
	X = abs(x2 - x1)

	for y in range(startY, startY+Y):
		for x in range(startX, startX+X):
			flag[y][x] = True

cnt = -1
arr = []


for x in range(N):
	for y in range(M):
		if(flag[y][x]==False):
			bfs(x, y, cnt)
			arr.append(cnt)
			cnt -=1
	
	
lists = list(itertools.chain.from_iterable(lists))

answer = []

for i in arr:
	answer.append(lists.count(i))
answer.sort()

print(len(answer))

for i in answer:
	print(i, end=" ")
