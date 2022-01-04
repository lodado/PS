from sys import setrecursionlimit, stdin
setrecursionlimit(10**6)
def scan():
	return list(map(int, stdin.readline().split()))
	
[N, M, K] = scan()

arr = []

def init(start, end, node):
	global tree, arr

	if(start==end):
		tree[node] = arr[start]
		return tree[node]

	mid = (start+end)//2
	tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
	return tree[node]

def find(start, end, node, left, right):
	global tree, arr
	
	if(right<start or left>end):
		return 0
	
	if(start>=left and end<=right):
		return tree[node]
	
	mid = (start+end)//2
	return find(start, mid, node*2, left, right)+ find(mid+1, end, node*2+1, left, right)

def update(start, end, node, index, diff):
	global tree
	
	if(start>index or end<index):
		return
	tree[node]+=diff

	if(start==end):
		return

	mid = (start+end)//2
	update(start, mid, node*2, index, diff)
	update(mid+1, end, node*2+1, index, diff)
	
for i in range(N):
	arr.append(int(stdin.readline()))

tree = [0 for i in range(len(arr)*4)]

init(0, len(arr)-1, 1)

for i in range(M+K):
	[a, b, c] = scan()
	if(a==1):
		update(0, len(arr)-1, 1, b-1, c-arr[b-1])
		arr[b-1]= c
	else:
		print(find(0, len(arr)-1, 1, b-1, c-1))
