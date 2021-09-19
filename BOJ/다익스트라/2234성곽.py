import sys
from collections import deque

def scan():
	return list(map(int,sys.stdin.readline().split()))
	
[row, col] = scan()

baseArr = []

visited = [[0 for j in range(row)] for i in range(col)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

div =[0b1000,0b0100,0b0010,0b0001] # 남 동 북 서 

maxi = -1
color = 1

dp = [0]

def bfs(startX, startY, color):
	global maxi
	if(visited[startY][startX]>0):
		return 0
	
	arr = deque([[startX, startY]])
	count = 0 
	
	dp.append([color, [startX,startY], count])
	while(arr):
		
		X, Y = arr.popleft()
		now = baseArr[Y][X]
		
		visited[Y][X] = color
		
		count+=1
		
		for i in range(4):
			if not(now & div[i]):
				newX = X + dx[i]
				newY = Y + dy[i]
				
				if(0<=newX<row and 0<=newY<col and visited[newY][newX]==0):
					visited[newY][newX] = color
					arr.append([newX, newY])
	
	if(count>maxi):
		maxi = count
	
	dp[color][2] = count
	return count

def start():
	global color
	for i in range(col):
		for j in range(row):
			pass
			if(bfs(j, i, color)>0):
				color+=1
	
for i in range(col):
	sc = []
	
	for j in scan():
		sc.append(j)
	baseArr.append(sc)

start()

print(color-1)
print(maxi)

maxi = -1

flag = []

for color, [startX, startY], space in dp[1:]:
	
	arr = deque([[startX, startY]])

	flag = [[0 for j in range(row)] for i in range(col)]
	
	while(arr):
		X, Y = arr.popleft()
		
		flag[Y][X] = True
		
		for i in range(4):
			
			newX = X + dx[i]
			newY = Y + dy[i]
			
			if(0<=newX<row and 0<=newY<col):
				
				if(visited[newY][newX]==color and flag[newY][newX]==False):
					flag[newY][newX] = True
					arr.append([newX, newY])
				
				if(visited[newY][newX]!=color):
					now = space + dp[visited[newY][newX]][2]
					
					if(maxi<now):
						maxi = now
					
print(maxi)
		
