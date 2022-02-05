from collections import defaultdict, deque
import math

def timeToMinute(time):
    hour, minute = map(int, time.split(':'))
    return hour * 60 + minute

def solution(fees, records):
    answer = []
    [baseMin, baseCost, addMin, addCost] = fees
    dic = defaultdict(deque)
    
    for record in records:
        [time, car, op] = record.split()
        dic[car].append([time, op])
    
    dic = sorted(dic.items(), key=lambda x:x[0])
    
    for key, value in dic:
        cost = baseCost
        totalWasteTime = -baseMin
        
        if(value[-1][1]=='IN'):
            value.append(['23:59','OUT'])
        
        while(value):
            startTime = timeToMinute(value.popleft()[0])
            endTime = timeToMinute(value.popleft()[0])
            totalWasteTime+=endTime-startTime
        
        if(totalWasteTime>0):
            cost+= math.ceil(totalWasteTime/addMin) * addCost
        answer.append(cost)
    
    return answer
