N = int(input())

arr = list(map(int, input().split()))

left = 0
right = len(arr)-1

ans = 0
while(left<right):
	ans = max(((right-left)-1)* min(arr[left],arr[right]), ans)
	if(arr[left]>arr[right]):
		right-=1
	else:
		left+=1
	
	
print(ans)
