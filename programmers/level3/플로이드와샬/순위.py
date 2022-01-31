def solution(n, results):
    answer = 0
    arr = [[0 for i in range(n+1)] for j in range(n+1)]
    
    for start, end in results: 
        arr[start][end] = 1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if(arr[i][k] and arr[k][j]):
                    arr[i][j] = 1
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if(arr[i][j] or arr[j][i]):
                count+=1
        if(count==n-1):
            answer+=1
                
    return answer
