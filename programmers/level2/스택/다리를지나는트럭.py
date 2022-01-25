from collections import deque

def solution(bridge_length, weight, truck_weights):
    count= 0
    totalWeight = 0
    deq = deque(truck_weights)
    trackDeque = deque()
    
    while(deq or trackDeque):
        
        for i in range(len(trackDeque)):
            trackDeque[i][1]+=1
        
        if(trackDeque):
            deqWeight, time = trackDeque[0]
            if(time>=bridge_length):
                totalWeight-=deqWeight
                trackDeque.popleft()
            
        if(deq and totalWeight+deq[0]<=weight):
            nowWeight = deq.popleft()
            totalWeight+= nowWeight
            trackDeque.append([nowWeight, 0])
        count+=1
    
    return count
