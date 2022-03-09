from sys import stdin
from collections import deque

N = int(input().rstrip())
K = int(input().rstrip())
dx = [0,-1,0,1]
dy = [-1,0,1,0]

sec = 0
nowDirection = 3
deq = deque([[1, 1]])

def scan():
	return list(map(int, stdin.readline().split()))

nodes = [[0 for i in range(N+1)] for j in range(N+1)]
apples = []
for i in range(K):
	y, x = scan()
	nodes[y][x] = 2

def canMove(deq):
	global N, nowDirection, dx, dy, nodes
	index = 0
	tail = False
	
	x, y = deq[0]
	newX = x + dx[nowDirection]
	newY = y + dy[nowDirection]
		
	if(0<newX<=N and 0<newY<=N and nodes[newY][newX]!=1):
		if(nodes[newY][newX]==2):
			tail=True
		deq.appendleft([newX, newY])
		nodes[newY][newX] = 1
	else:
		return False
		
	if not(tail):
		beforeX, beforeY = deq.pop()
		nodes[beforeY][beforeX] = 0
		
	return True
	
L = int(input().rstrip())
direct = deque([])
for i in range(L):
	sc= list(input().split())
	direct.append([int(sc[0]), sc[1]])

nodes[1][1] = 1

while(True):
	
	flag = canMove(deq)
	if not(flag):
		break
	sec+=1
	
	if(direct and direct[0][0]==sec):
		_, d = direct.popleft()
		if(d=='L'):
			nowDirection = (nowDirection + 1) % 4
		else:
			nowDirection -= 1
			if(nowDirection<0):
				nowDirection = 3


print(sec+1)
