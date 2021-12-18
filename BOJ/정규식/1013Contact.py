import re
p = re.compile('ab+')
N = int(input())
for _ in range(N):
	rd = input()
	print('YES' if re.fullmatch('(100+1+|01)+', rd) else 'NO')
