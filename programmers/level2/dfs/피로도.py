from sys import setrecursionlimit
setrecursionlimit(10**9)
isVisited = None

def searchDungeon(length, stat, dungeons, index):
    global isVisited
    answer = length
    
    for i in range(len(dungeons)):
        minReqStat, cost = dungeons[i]
        if(stat>=minReqStat and cost<=stat and not isVisited[i]):
            isVisited[i] = True
            answer = max(answer, searchDungeon(length+1, stat-cost, dungeons, i+1))
            isVisited[i] = False
    return answer
    
def solution(k, inputs):
    global isVisited
    dungeons = sorted(inputs, key=lambda x:(-x[0]))
    isVisited = [False for i in range(len(inputs))]
    answer = searchDungeon(0, k, dungeons, 0)
    return answer
