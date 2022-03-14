from sys import stdin

def scan():
	return list(map(int, stdin.readline().split()))
	
for i in range(4):
	[x1, y1, x2, y2, x3, y3, x4, y4] = scan()
	
	leftX1 = max(x1, x3)
	leftY1 = max(y1, y3)
	rightX2 = min(x2, x4)
	rightY2 = min(y2, y4)
	
	dx, dy = (rightX2-leftX1), (rightY2-leftY1)
	
	if(dx>0 and dy>0):
		print('a')
	elif(dx<0 or dy<0):
		print('d')
	elif(dx==0 and dy==0):
		print('c')
	else:
		print('b')
