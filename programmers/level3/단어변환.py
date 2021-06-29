from collections import deque
import copy

def solution(begin, target, words):
    
    deq = deque()
    deq.append((begin, 0))
    
    alphabet =sorted("qwertyuiopasdfghjklzxcvbnm")
    
    newwords = copy.deepcopy(words)
    
    while(len(deq)>0):
        
        current, index = deq.popleft()
        #print(current, index)

        if(current==target):
            return index
        if(index>=len(words)):
            continue
        
        for string in range(len(current)):
            
            for alpha in alphabet:
                newstr = current[:string]+alpha+current[string+1:]
                for aa in newwords:
                    if newstr == aa:
                        newwords.remove(newstr)
                        deq.append((newstr,index+1))
    return 0
