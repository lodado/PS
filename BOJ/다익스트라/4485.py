import sys
import heapq

def scan():
	return list(map(int, sys.stdin.readline().split()))
	
dx = [0,0,1,-1]
dy = [1,-1,0,0]

count = 1 

while(True):
	
	[N] = scan()
	if(N==0):
		break
	
	arr = [[j for j in scan()] for i in range(N)]
	dp = [ [sys.maxsize for j in range(N)] for i in range(N)]
	startX = 0
	startY = 0
	
	hq = [[0, startX, startY]]
	dp[0][0] = arr[0][0]
	
	while(hq):
		
		cost, nowX, nowY = heapq.heappop(hq)
		for X,Y in zip(dx, dy):
			
			newX = nowX + X 
			newY = nowY + Y
			if(0<=newX<N and 0<=newY<N):
				
				if(dp[newY][newX]>dp[nowY][nowX] + arr[newY][newX]):
					dp[newY][newX] = dp[nowY][nowX] + arr[newY][newX]
					heapq.heappush(hq, [dp[nowY][nowX] + arr[newY][newX], newX, newY])
				
	print('Problem %d: %d'%(count, dp[N-1][N-1]))		
	count+=1		
			
			
		
		
