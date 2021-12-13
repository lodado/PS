from sys import maxsize

def solution(n, s, a, b, fares):
    answer = 0
    dist = [[maxsize for i in range(n)] for j in range(n)]
    
    for start, end, value in fares:
        dist[start-1][end-1] = value
        dist[end-1][start-1] = value
    
    for i in range(n):
        dist[i][i] = 0
    
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(dist[i][j]>dist[i][k]+dist[k][j]):
                    dist[i][j]=dist[i][k]+dist[k][j]

    ans = maxsize
    for i in range(n):
        ans = min(ans, dist[s-1][i]+dist[i][a-1]+dist[i][b-1])
    return ans
