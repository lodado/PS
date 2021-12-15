from sys import stdin

def scan():
	return stdin.readline()

def scanList():
	return list(map(int, scan().split()))

N = int(scan())
M = int(scan())

nodes = [i for i in range(N+1)]
arr = []

def findParent(index):
	global nodes
	if(index==nodes[index]):
		return index
	nodes[index] = findParent(nodes[index])
	return nodes[index]

def setParent(a, b):
	a = findParent(a)
	b = findParent(b)
	
	if(a>b):
		nodes[a] = b
	elif(a==b):
		return False
	else:
		nodes[b] = a
		
	return True

for i in range(M):
	[start, end, cost] = scanList()
	arr.append((cost, start, end))

arr.sort()
ans = 0

for (cost, start, end) in arr:
	if(setParent(start, end)):
		ans+=cost
print(ans)
