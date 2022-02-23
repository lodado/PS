def isVaild(stones, mid, k):
    
    count = 0
    for stone in stones:
        if(stone-mid<=0):
            count+=1
        else:
            count=0
        
        if(k<=count):
            break
        
    return count
                

def solution(stones, k):
    answer = 0
    left = 0
    right = 200000000
    
    while(left<=right):
        mid = (left+right)//2
        count = isVaild(stones, mid, k)
        
        if (count<k):
            left = mid + 1
        else:
            right = mid-1 

    return left
