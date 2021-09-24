import heapq

def solution(genres, plays):
    answer = []
    
    dicts = {}
    
    index = 0 
    for i,j in zip(genres, plays):
        if not(dicts.get(i)):
            dicts[i]=[0, []]
        dicts[i][0]+=j
        
        heapq.heappush(dicts[i][1], [-j, index])
        index+=1
    
    lis = sorted(list(dicts.items()), key=lambda x:x[1][0], reverse=True)
    
    print(lis)
    
    for i, arr in lis:
        
        now = arr[1]
        
        count = 0 
        while(len(now)>0 and count<2):
            answer.append((heapq.heappop(now)[1]))
            count+=1
        
    return answer
