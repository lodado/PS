from sys import stdin

def scan():
	return list(map(int, stdin.readline().split()))
	
[N]= scan()
arr = scan()
answer = [-1 for i in range(N)]

st = []

index = len(arr)-1

while(index>=0):
	st.append(arr[index])
	index-=1
	
	while(st and index>=0):
		now = arr[index]
		if(st and st[-1]>now):
			answer[index] = st[-1]
			st.append(now)
			index-=1
		else:
			st.pop()

print(*answer)
