from collections import deque

def solution(n, t, m, p):
    
    ans = ['0']
    answer = []
    
    for i in range(0, m*t):
        deq = deque([])
        while(i>0):
            result = i%n
            if(10<=result<=15):
                result = chr(65+result-10)
            deq.appendleft(str(result))
            i = i//n
        ans+=deq
    
    count=0
    
    for i in range(p-1, len(ans), m):
        if(count>=t):
            break
        answer.append(ans[i])
        count+=1
    
    return ''.join(answer)
