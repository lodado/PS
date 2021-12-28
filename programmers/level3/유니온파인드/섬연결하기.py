import copy
from sys import setrecursionlimit
setrecursionlimit(10**6)
parents = []

def findParent(num):
    global parents
    
    if(parents[num]==num):
        return num
    
    parents[num] = findParent(parents[num])
    return parents[num]

def solution(n, costs):
    global parents
    ans = 0
    
    adj = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for start, end, cost in costs:
        adj[start][end] = cost
        adj[end][start] = cost   
    
    parents = [i for i in range(n+1)]
    
    cst = sorted(costs, key=lambda x:x[2])
            
    for start, end, cost in cst:
        a = findParent(start)
        b = findParent(end)
        
        if(a>b):
            parents[a] = b
        elif(a==b):
            continue
        else:
            parents[b] = a
        
        ans+=cost
        
    return ans
