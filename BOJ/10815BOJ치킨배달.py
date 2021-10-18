def scan():
	return map(int, input().split())

def binary_search(arr, val):
	
	left = 0
	right = len(arr)-1
	
	while(left<=right):
		
		mid = (right + left)//2
	#	print(left, mid, right)
		
		now = arr[mid]
		
		if(now<val):
			left = mid + 1
		elif(now==val):
			return 1
		else:
			right = mid - 1
	#print()
	return 0



N = scan()

baseArr = sorted([i for i in scan()])

M = scan()

findArr = [i for i in scan()]

for i in findArr:
	a = binary_search(baseArr, i)
	print(a, end=' ')
