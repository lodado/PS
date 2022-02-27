def solution(people, limit):
    answer = 0
    ppl = sorted(people)
    left, right = 0, len(ppl)-1
    
    while(left<=right):
        value = ppl[left] + ppl[right]
        
        if(value<=limit):
            left+=1
        answer+=1
        right-=1
    return answer
