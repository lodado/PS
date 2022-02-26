from sys import stdin
from collections import deque
import copy

def scan():
	return list(map(int,  stdin.readline().split()))

[N] = scan()
arr = [scan() for i in range(N)]

dx = [1,-1,0,0] ## 동 서 남 북
dy = [0,0,1,-1]

answer = 0

def push(deq, x, y):
	global arr
	if(arr[y][x]>0):
		deq.append(arr[y][x])
		arr[y][x] = 0


# 동:0 서:1 남:2 북:3
def merge(deq, x, y, direction):
	global arr, dx, dy
	
	while(deq):
		now = deq.popleft()
		if(arr[y][x]==0):
			arr[y][x] = now
		elif(arr[y][x]==now):
			arr[y][x] = now * 2
			x = x + dx[direction]
			y = y + dy[direction]
		else:
			x = x + dx[direction]
			y = y + dy[direction]
			arr[y][x] = now


# 동:0 서:1 남:2 북:3
def move(direction):
	global N, arr
	
	if(direction==0):
		for y in range(N):
			deq = deque([])
			for x in range(N):
				push(deq, x, y)
			merge(deq, 0, y, 0)
	if(direction==1):
		for y in range(N):
			deq = deque([])
			for x in range(N-1, -1, -1):
				push(deq, x, y)
			merge(deq, N-1, y, 1)
	else:	# 필요없는데 잘못넣음
		if(direction==2):
			for x in range(N):
				deq = deque([])
				for y in range(N):
					push(deq, x, y)
				merge(deq, x, 0, 2)
		if(direction==3):
			for x in range(N):
				deq = deque([])
				for y in range(N-1, -1, -1):
					push(deq, x, y)
				merge(deq, x, N-1, 3)
			

def dfs(count):
	global answer, arr, N
	
	if(count==5):
		for y in range(N):
			for x in range(N):
				answer = max(answer, arr[y][x])
		return
	
	arrClone = copy.deepcopy(arr)
	
	for i in range(4):
		move(i)
		dfs(count+1)
		arr = copy.deepcopy(arrClone)

dfs(0)
print(answer)
