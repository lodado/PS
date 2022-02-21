def solution(inputs):
    answer = 0
    
    routes = sorted(inputs, key=lambda x:x[1])
    locate = -30001
    
    for start, end in routes:
        if(locate<start):
            locate = end
            answer+=1
    return answer
