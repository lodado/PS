from sys import stdin

def scan():
	return list(map(int, stdin.readline().split()))
	
arr = [scan() for i in range(19)]
markDirection = [[[-1 for i in range(4)] for d in range(19)] for d in range(19)]
dx = [1,1,0,-1]
dy = [0,1,1,1]
N = 19

def dfs(x, y, length, val, direction, container=[]):
	global arr, markDirection 
	
	newX = x + dx[direction]
	newY = y + dy[direction] 
	
	if(0<=newX<N and 0<=newY<N and arr[newY][newX]==val and markDirection[y][x][direction]==-1):
		markDirection[y][x][direction] = direction
		container.append([newY, newX])
		return dfs(newX, newY, length+1, val, direction, container)
	else:
		markDirection[y][x][direction] = direction
		return [length, direction, container]

ans = None
	
def rotate():
	global ans, arr, N, dx, dy, markDirection
	for y in range(N):
		for x in range(N):
			if(arr[y][x]>0):
				for direction in range(4):
					newX = x + dx[direction]
					newY = y + dy[direction]
					
					if(0<=newX<N and 0<=newY<N and arr[y][x]==arr[newY][newX] and markDirection[y][x][direction]==-1):
						[length, direct, container] = dfs(newX, newY, 2, arr[y][x], direction, [[y, x], [newY, newX]])
						markDirection[y][x][direction] = direction
						if(length==5):
							ans = [arr[y][x], container]
							return

rotate()

if(ans):
	ans[1].sort(key = lambda x:(x[1], x[0]))
	print(ans[0])
	print(ans[1][0][0]+1, ans[1][0][1]+1)
else:
	print(0)
