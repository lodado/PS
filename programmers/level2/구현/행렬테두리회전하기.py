from sys import maxsize 
value = 0

def autoIncrement():
    global value
    value+=1
    return value

def solution(rows, columns, queries):
    answer = []
    
    arr = [[autoIncrement() for _ in range(columns)] for _ in range(rows)]
    
    for query in queries:
        y1, x1, y2, x2 = map(lambda x:x-1, query)
        mini = maxsize
        
        firstValue = arr[y1][x1]
        
        for newY in range(y1, y2):
            tmp = arr[newY+1][x1]
            arr[newY][x1] = tmp
            mini = min(tmp, mini)
            
        for newX in range(x1, x2):
            tmp = arr[y2][newX+1]
            arr[y2][newX] = tmp
            mini = min(tmp, mini)
        
        for newY in range(y2, y1, -1):
            tmp = arr[newY-1][x2]
            arr[newY][x2] = tmp
            mini = min(tmp, mini)
        
        for newX in range(x2, x1, -1):
            tmp = arr[y1][newX-1]
            arr[y1][newX] = tmp
            mini = min(tmp, mini)
            
        arr[y1][x1+1] = firstValue
        mini = min(mini, firstValue)
        answer.append(mini)
    
    return answer
