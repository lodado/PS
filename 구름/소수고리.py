# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from itertools import permutations

prime = [2,3,5,7,11,13,17,19]
user_input = int(input())


arr = [i for i in range(2, user_input+1)]

a = list(permutations(arr))

for lists in a:
	flag = True
	
	lists = (1, *lists)
	
	for i in range(len(lists)):
		
		if(i+1<len(lists) and lists[i]+lists[i+1] not in prime):
			flag = False
			break
		if(i>=1 and lists[i]+lists[i-1] not in prime):
			flag=False
			break
	
	if(lists[0] + lists[-1] not in prime):
		flag=False
	
	if(flag):
		print(*lists)	
		
		
	
