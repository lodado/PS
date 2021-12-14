from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

def scan():
	return list(map(int, stdin.readline().split()))

[N, M] = scan()

nodes = [i for i in range(N+1)]
def getParent(index):
	global nodes
	if(nodes[index]==index):
		return index
	nodes[index] = getParent(nodes[index])
	return nodes[index]

for _ in range(M):
	[op, first, second] = scan()
	first, second = min(first, second), max(first, second)
	fInd = getParent(first)
	sInd = getParent(second)
	if(op==0):
		nodes[sInd] = fInd
	else:
		if(fInd == sInd):
			print("YES")
		else:
			print('NO')
