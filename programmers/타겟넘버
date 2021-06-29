from collections import deque

def solution(numbers, target):
    
    deq = deque()
    
    deq.append((0, 0))
    
    count=0
    
    while(len(deq)>0):
        
        total, index = deq.popleft()
        
        if(index==len(numbers)):
            if(target == total):
                count+=1
            continue
        
        now = numbers[index]
        
        deq.append((total+now, index+1))
        deq.append((total-now, index+1))

    return count
