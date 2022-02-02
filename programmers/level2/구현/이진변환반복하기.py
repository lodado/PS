def solution(inputs):
    s = inputs
    answer = []
    
    while(s!='1'):
        count = s.count('0')
        answer.append(count)
        s= str(bin(len(s)-count)[2:])  
        
    return [len(answer), sum(answer)]
