from sys import stdin

def scan():
	return list(map(int, stdin.readline().split()))

while(True):
	arr = scan()
	
	if(len(arr)==1 and arr[0]==0):
		break
	
	arr = arr[1:]
	
	st = []
	ans = 0
	
	for i in range(len(arr)):
		now = arr[i]
		
		while(st and arr[st[-1]]>now):
			topIndex = st.pop()
			if not(st):
				width = i
			else:
				width = i - st[-1] - 1
			ans = max(ans, width * arr[topIndex])
		st.append(i)
	
	while(st):
		topIndex = st.pop()
		if not(st):
			width = len(arr)
		else:
			width = len(arr) - st[-1] - 1
		ans = max(ans, width * arr[topIndex])
	
	print(ans)
	
	
