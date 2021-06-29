def solution(s):
   
    allLen = len(s)
    N = len(s)//2
    maxim = 987654321
    
    for i in range(1, N+1):
        #print(i)
        splits = []
        
        for j in range(0, allLen, i):
            splits.append((s[j:j+i]))
        
        #print(splits)
        news = ""
        count = 1
        
        for index in range(0,len(splits)):
            
            if(count>1):
                count-=1
                continue
            
            #print(splits[index],end = " : ")
            newsplits = splits[index+1:] 
            
            for k in newsplits:
                if(splits[index] == k):
                    count+=1
                #    print(k, end=" ")
                else:
                    break
                    
            if(count!=1):
                news+=str(count)+splits[index]
            else:
                news+=splits[index]
        #print(news)
        
        maxim = min(maxim, len(news))
        
    return maxim if maxim!=987654321 else 1