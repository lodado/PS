import heapq
maxQ = []
minQ = []

def insert(num):
    global maxQ, minQ
    heapq.heappush(maxQ, -num)
    heapq.heappush(minQ, num)

def pop(num):
    global maxQ, minQ
    if not(maxQ and minQ):
        return
    
    if(num==-1):
        maxQ.remove(-heapq.heappop(minQ))
    else:
        minQ.remove(-heapq.heappop(maxQ))
    
def solution(operations):
    global maxQ, minQ
    
    for op in operations:
        command, num = op.split()
        num = int(num)
        
        if(command=="I"):
            insert(num)
        else:
            pop(num)
    
    answer = [0, 0] if not(maxQ and minQ) else [-maxQ[0], minQ[0]]
    return answer
