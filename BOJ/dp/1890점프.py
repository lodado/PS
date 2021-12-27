from collections import deque

N= int(input())

def scan():
	return list(map(int, (input().split())))

arr = [scan() for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

dx = [1,0]
dy = [0,1]

dp[0][0]= 1

for i in range(N): # 세로 
	for j in range(N): #가로
		if(dp[i][j]==0 or (i==N-1 and j==N-1)):
			continue
		
		now = arr[i][j]
		
		for z in range(2):
			newX = j + dx[z] * now
			newY = i + dy[z] * now
			if(0<=newX<N and 0<=newY<N):
				dp[newY][newX] += dp[i][j]

print(dp[N-1][N-1])
