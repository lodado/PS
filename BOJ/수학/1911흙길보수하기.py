import math

def scan():
	return map(int, input().split())
	
N, M = scan()
arr = [list(scan()) for i in range(N)]
ans = 0

arr.sort(key=lambda x:x[0])
remain = 0

for s, e in arr:
	if(s<=remain):
		s = remain + 1
	if(e<=s):
		continue
	cnt = math.ceil((e-s)/M)
	ans += cnt
	remain = max(remain, s+cnt*M-1)
print(ans)
