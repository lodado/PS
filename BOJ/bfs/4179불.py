from sys import stdin
from collections import deque

def scan():
	return stdin.readline().strip()

[N, M] = list(map(int, scan().split()))

arr = []
# 세로 가로
F = []
J = []

for i in range(N):
	now = list(scan())
	for index, j in enumerate(now):
		if(j=='J'):
			J.append((i, index, 0, 'J'))
		elif(j=='F'):
			F.append((i, index, 0, 'F'))
	
	arr.append(now)

def bfs():
	global arr
	global N
	global M
	global F
	global J
	dx = [0,0,1,-1]
	dy = [1,-1,0,0]
	deq = deque([*F, *J])
	visited = [[False for i in range(M)] for j in range(N)]
	
	while(deq):
		startY, startX, count, value = deq.popleft()
		
		if(value=='J'):
			if(visited[startY][startX]):
				continue
			visited[startY][startX] = True
		
		for i in range(4):
			newX = startX + dx[i]
			newY = startY + dy[i]
			
			if(value=="J" and not (0<=newX<M and 0<=newY<N)):
				return count+1
			if((0<=newX<M and 0<=newY<N)):
				nextBlock = arr[newY][newX]
				
				if(nextBlock!='F' and nextBlock!='#'):
					arr[newY][newX] = value
					
					deq.append((newY, newX, count+1, value))
	
	return 'IMPOSSIBLE'
	
print(bfs())
