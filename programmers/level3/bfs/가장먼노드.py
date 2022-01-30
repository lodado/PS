from collections import deque
from sys import maxsize

def solution(n, edge):
    answer = 0
    
    arr = [[] for _ in range(n+1)]
    isVisited = [maxsize for _ in range(n+1)]
    
    for start, end in edge:
        arr[start].append(end)
        arr[end].append(start)
    
    deq = deque([[1, 0]])
    isVisited[1] = 0
    maxi = 0
    
    while(deq):
        nowVal, count = deq.popleft()
        if(maxi<count):
            maxi = count
        
        for nextVal in arr[nowVal]:
            if (isVisited[nextVal]>count+1):
                isVisited[nextVal] = count+1
                deq.append([nextVal, count+1])
        
    return isVisited.count(maxi)
