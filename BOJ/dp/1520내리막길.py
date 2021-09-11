import sys

sys.setrecursionlimit(1000000)

def scan():
	return map(int, sys.stdin.readline().split())

M, N = scan() #세로의 크기 M과 가로의 크기 N

arr = [[0] for i in range(M+1)]

for i in range(1, M+1):
	
	arr[i].extend(list(scan()))

dp = [[-1 for j in range(0, N+1)] for i in range(M+1)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x, y):
	
	if(y==M and x==N):
		return 1
	
	if(dp[y][x]==-1):
		dp[y][x] = 0
		for i in range(4):
			newX = x + dx[i]
			newY = y + dy[i]
		
			if(0<newX<=N and 0<newY<=M):
				if(arr[y][x]>arr[newY][newX]):
					dp[y][x]+= dfs(newX, newY)
			
	
	return dp[y][x]


dfs(1,1)

print(dp[1][1])



	
	
