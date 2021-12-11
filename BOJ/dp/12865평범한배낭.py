import sys

count = 0
item = [[]]
N=0
K=0

while(True):
	insert = sys.stdin.readline()
	if not (insert):
		break
	count+=1
	num, value = map(int, insert.split())
	if(count==1):
		N = num
		K = value
	else:
		item.append([num, value])

dp = [[0 for _ in range(K+1)] for _ in range(count)]

for i in range(1, count):
	weight, value = item[i]
	
	for j in range(K+1):
		if(j<weight):
			dp[i][j] = dp[i-1][j]
		else:
			dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)

print(dp[N][K])	
