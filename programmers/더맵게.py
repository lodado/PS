import heapq as hq

def solution(scoville, K):

    count =0
    
    que = scoville[:]
    hq.heapify(que)
    
    while(True):
        if(len(que)<2):
            return -1
        
        getscoba = hq.heappop(que) + 2 * hq.heappop(que) 
        
        hq.heappush(que, getscoba)
        count+=1
        
        if(que[0]>=K):
            return count
