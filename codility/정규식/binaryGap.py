import re

def solution(N):
    
    arr = re.findall(r'10+(?=1)', bin(N)[2:])
    arr.sort()
    return len(arr[-1])-1 if arr else 0
