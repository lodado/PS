from collections import deque

def timeToNumber(time):
    return int(time[:2])*60+int(time[3:])
    
def solution(n, t, m, timetable):
    
    arr = deque(sorted([timeToNumber(time) for time in timetable]))
    
    nowTime = 540
    index = 0
    cnt = 0
    ind=0
    while(index<n):
        cnt = 0
        while(ind<len(arr) and arr[ind]<=nowTime and cnt<m):
            cnt+=1
            ind+=1
        if(cnt<m):
            ans = nowTime
        else:
            ans = arr[ind-1]-1
            
        index+=1
        nowTime += t
    answer = '%02d:%02d'%(ans//60, ans%60)
    return answer
