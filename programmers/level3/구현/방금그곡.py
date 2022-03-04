def timeToSec(time):
    hours, minute = time.split(':')
    return int(minute) + int(hours)*60
    
def solution(m, musicinfos):
    ans = []
    m = list(m)
    cmpList = []
    for i in m:
        if(i=='#'):
            cmpList[-1]+='#'
        else:
            cmpList.append(i)
    
    for ind, i in enumerate(musicinfos):
        startTime, endTime, name, content = i.split(',')
        sec = timeToSec(endTime) - timeToSec(startTime)
        totalTime = sec
        
        lyrics = []
        index = 0
        
        while(sec>0):
            now = content[index]
            if(index+1<len(content) and content[index+1]=='#'):
                now +='#'
                index+=1
            lyrics.append(now)
            index+=1
            sec-=1
            if(index>=len(content)):
                index = index % len(content)
        
        index = 0
        
        for lyric in lyrics:
            if(lyric==cmpList[index]):
                index+=1
            else:
                index=0
                if(cmpList[0]==lyric):
                    index+=1
                
            if(index>=len(cmpList)):
                ans.append([-totalTime, ind, name])
                break
    
    ans.sort(key=lambda x:(x[0], x[1]))
    return ans[0][2] if ans else '(None)'
