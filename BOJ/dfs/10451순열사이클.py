from sys import stdin, setrecursionlimit
from collections import Counter
setrecursionlimit(10**9)

def scan():
	return list(map(int, stdin.readline().split()))
	
T = int(input())
ans = 0

def dfs(arr, visited, startNumber, number):
	global ans
	
	if(startNumber == number):
		visited[number] = True
		ans+=1
		return
	nextNumber = arr[number]
	
	if not(visited[i]):
		dfs(arr, visited, startNumber, nextNumber)
	
	visited[number]=True
		
for _ in range(T):
	N = int(input())
	ans = 0
	visited = [False for i in range(N+1)]
	visited[0] = True
	
	arr = [0] + scan()
	
	for i in range(1, len(arr)):
		if not(visited[i]):
			dfs(arr, visited, i, arr[i])
			
	print(ans)
