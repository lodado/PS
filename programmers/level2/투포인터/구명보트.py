def solution(people, limit):
    answer = 0
    ppl = sorted(people)
    left, right=0, len(ppl)-1
    
    while(left<=right):
        answer+=1
        if(ppl[left]+ppl[right]<=limit):
            left+=1
        right-=1
        
    return answer
