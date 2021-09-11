import sys

def scanInt():
	return list(map(int, sys.stdin.readline().split()))
	
[N, M] = scanInt()

arr = [[0 for j in range(N+1)] for i in range(N+1)]

for i in range(1, M+1):
	[first, second] = scanInt()
	arr[first][second] = 1

for i in range(1, N+1):
	for j in range(1, N+1):
		for z in range(1, N+1):
			if(arr[j][i] and arr[i][z]):
				arr[j][z] = 1

ans = 0

for i in range(1, N+1):
	count = 0
	
	for j in range(1, N+1):
		if(i!=j):
			if(arr[i][j] or arr[j][i]):
				count+=1
	
	if(N-1==count):
		ans+=1	

print(ans)
