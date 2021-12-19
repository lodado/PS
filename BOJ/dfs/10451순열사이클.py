from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

def scan():
	return stdin.readline()
	
def scanList():
	return list(map(int, scan().split()))

ans = 0

def dfs(findNumber, index, arr):
	global ans
	
	if(arr[index][2]):
		return
	
	nowValue = arr[index][1]
	
	if(nowValue == findNumber):
		ans+=1
		return
	
	arr[index][2] = True
	
	dfs(findNumber, nowValue, arr)	
		
		
for _ in range(int(scan())):
	N = int(scan())
	arr = [[0,0,True]] + [[index+1, value, False] for index, value in enumerate(scanList())]
	
	for index, value, check in arr:
		if not check:
			dfs(index, index, arr)
	
	print(ans)
	ans =0
