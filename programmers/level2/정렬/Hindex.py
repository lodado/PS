def solution(citations):
    answer = 0
    
    counts = [0 for i in range(10001)]
    length = len(citations)
    
    sums = 0
    
    for i in citations:
        counts[i]+=1
        sums+=i

    ind = 0
    ref = 0
    
    for now in range(10001):
        
        nowCount = counts[now]
        
        left = ref
        ref += nowCount
        right = length - ref
        
        if(left<=now and right+nowCount>=now):
            answer = now
        
    return answer
