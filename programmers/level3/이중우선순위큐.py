import heapq

def solution(operations):
    answer = []
    
    maxQ = []
    minQ = []
    
    for i in operations:
        
        pars = i.split(' ')
        
        if(pars[0]=='I'):
            heapq.heappush(maxQ, -int(pars[1]))
            heapq.heappush(minQ, int(pars[1]))
        
        if(pars[0]=="D"):
            
            if(len(maxQ)<=0 or len(minQ)<=0):
                continue
            
            if(pars[1]=='1'):
                now = -heapq.heappop(maxQ)
                minQ.remove(now)
            else:
                now = -heapq.heappop(minQ)
                maxQ.remove(now)
    
    return [-maxQ[0] if maxQ else 0, minQ[0] if minQ else 0]
