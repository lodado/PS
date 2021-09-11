import sys

def scan():
	return map(int, sys.stdin.readline().split())

N, M = scan()



adj = [[0 for j in range(N+1)] for i in range(N+1)] 
adjn = [[0 for j in range(N+1)] for i in range(N+1)] 


count = 0

def dfs(value, visited, arr):
	
	global count;

	visited[value] = True
	
	for i in range(1, N+1):
		
		next = arr[value][i]

		if(visited[next]):
			continue
		
		if(next):

			count+=1
			dfs(next, visited, arr)

for i in range(M):
	
	first, second = scan()
	adj[first][second] = second
	adjn[second][first] = first

ans = 0 

for i in range(1,N+1):
	flag = [False for a in range(N+1)]
	flagn = [False for a in range(N+1)]

	dfs(i, flag, adj)
	
	dfs(i, flagn, adjn)
	
	if(N-1==count):
		ans+=1
	count=0



print(ans)	
