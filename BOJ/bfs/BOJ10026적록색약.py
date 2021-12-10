from sys import stdin
from collections import deque

def scan():
	return stdin.readline()
	
def scanList():
	return scan().strip()

N = int(scan())

def bfs(startX, startY, myBox, isVisited):
	global N
	
	if(isVisited[startY][startX]):
		return False
	
	dx = [0,0,1,-1]
	dy = [1,-1,0,0]
	
	deq = deque([[startX,startY]])
	myColor = myBox[startY][startX]
	
	flag = False
	
	while(deq):
		x, y = deq.popleft()
		
		isVisited[y][x] = True
		
		for i in range(4):
			flag=True
			newX = x + dx[i]
			newY = y + dy[i]
		
			
			if(0<=newX<N and 0<=newY<N):
				if(not isVisited[newY][newX] and myBox[newY][newX]==myColor):
					isVisited[newY][newX]= True
					deq.append([newX, newY])
			
	return flag
		

box = []
rBox = []

for _ in range(N):
	now = scanList()
	cont1 = []
	cont2 = []
	for i in now:
		if(i in 'RG'):
			cont1.append('R')
		else:
			cont1.append(i)
		cont2.append(i)
	rBox.append(cont1)
	box.append(cont2)

isVisited1=[[False for _ in range(N)] for _ in range(N)]
isVisited2=[[False for _ in range(N)] for _ in range(N)]

cnt1 = 0
cnt2 = 0

for i in range(N):
	for j in range(N):
		if(bfs(i,j, box, isVisited1)):
			cnt1+=1
		if(bfs(i,j, rBox, isVisited2)):
			cnt2+=1
print(cnt1, cnt2, end=" ")		
