from sys import setrecursionlimit
from collections import Counter
setrecursionlimit(10**6)

arr = None

def getParent(index):
    global arr
    
    if(arr[index]==index):
        return index
    
    arr[index] = getParent(arr[index])
    return arr[index]

def findParent(first, second):
    
    if(first>second):
        second, first = first, second
    
    first = getParent(first)
    second = getParent(second)
    
    arr[second] = arr[first]
    
    
def solution(n, computers):
    global arr
    answer = 0
    
    arr = [i for i in range(n)]
    
    for i, computer in enumerate(computers):
        for j in range(len(computer)):
            if(computer[j]==1):
                findParent(j, i)
    
    for i in range(n):
        arr[i] = getParent(i)
    
    return len(Counter(arr))
