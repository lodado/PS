import math

def solution(n, times):
    answer = 0

    low, high = 0, max(times)*n

    while(low<=high):
        total = 0 

        mid = (low + high)//2

        for i in times:
            total+=math.floor(mid/i)

        if(total>=n):
            high = mid-1
        else:
            low = mid+1

    return low
