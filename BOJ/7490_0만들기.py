import copy
from collections import deque

N = int(input())

allans = []

def bfs(end):

	que = deque([[1, []]])

	while(que):
	
		now, arr = que.popleft()
		
		if(now>=end):
			
			
			st = deque([i for i in range(1, end+1)])
			ans = deque([i for i in range(1, end+1)])
			
			ind = 0
			fin = end
			index = 0
			
			while(ind<fin-1):
				
				if(arr[index]==' '):
					st[ind] = int(str(st[ind]) + str(st[ind+1]))
					del st[ind+1]
					fin-=1
				else:
					ind+=1
				index+=1
						
			result = st.popleft()
			
			for i in filter(lambda x: x!=' ', arr):
				if(i=='+'):
					result+= st.popleft()
				else:
					result-= st.popleft()
			
			if(result==0):
				
				nowans = []
				
				for i, j in zip(ans, arr):
					nowans.append(str(i)+j)
				nowans.append(str(end))
				
				allans.append("".join(nowans))
			
			continue
			
		newarr = copy.deepcopy(arr)	
		
		que.append([now+1, newarr+['+']])
		que.append([now+1, newarr+['-']])
		que.append([now+1, newarr+[' ']])
		
		
		
for i in range(N):
	allans=[]
	
	end = int(input())
	
	bfs(end)
	
	for j in sorted(allans):
		print(j)
	print()
		
