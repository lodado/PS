from collections import deque
from sys import maxsize

maxSquareSize = 102

def bfs(arr, characterX, characterY, itemX, itemY):
    global maxSquareSize
    
    answer = maxsize
    deq = deque([[characterX, characterY, 0]])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    while(deq):    
        nowX, nowY, value = deq.popleft()
        
        if(answer<=value):
            continue

        for i in range(4):
            newY = nowY + dy[i]
            newX = nowX + dx[i]
            
            if(0<=newY<maxSquareSize and 0<=newX<maxSquareSize):
                if(itemY==newY and itemX==newX):
                    answer = min(answer, value+1)
                    continue
                
                if(arr[newY][newX]==1):
                    arr[newY][newX]=2
                    deq.append([newX, newY, value+1])
                    
    return answer

def solution(rectangle, characterX, characterY, itemX, itemY):
    global maxSquareSize 
    answer = 0
    characterX, characterY, itemX, itemY = characterX*2, characterY*2, itemX*2, itemY*2
    
    arr = [[0 for i in range(maxSquareSize)] for i in range(maxSquareSize)]
    
    ret = [[x1*2, y1*2, x2*2, y2*2] for x1, y1, x2, y2 in rectangle] 
    
    for x1, y1, x2, y2 in ret:
        for newX in range(x1, x2+1):
            arr[y2][newX] = 1
            arr[y1][newX] = 1 
            
        for newY in range(y1, y2+1):
            arr[newY][x1] = 1
            arr[newY][x2] = 1
        
    for x1, y1, x2, y2 in ret:
        for newY in range(y1+1, y2):
            for newX in range(x1+1, x2):
                arr[newY][newX] = 0
    
    answer = bfs(arr, characterX, characterY, itemX, itemY)  
    return answer // 2
