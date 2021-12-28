import re

def timeToNumber(h, m, s, ss, t):
    end = int(h) *3600*1000 + int(m)*60*1000 + int(s)*1000 + int(ss)
    
    T = int(float(t)*1000)
    start= end - T + 1
    if(start<0):
        return [0, end]
    else:
        return [start, end]

def solution(lines):
    answer = 0
    ans = []
    
    for line in lines:   
        (h, m, s, ss, t) = re.search('(\d\d):(\d\d):(\d\d).(\d\d\d) (\d+|\d+.\d+)s', line).groups()
        ans.append(timeToNumber(h, m, s, ss, t))
    maxi = 0
    for ind, [start, end] in enumerate(ans):
        fin = end + 1000
        cnt = 0
        for newStart, newEnd in ans[ind:]:
            
            if(newStart<fin):
                cnt+=1 
        maxi = max(maxi, cnt)

    return maxi
