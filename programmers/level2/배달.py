import heapq

class nodes:
    def __init__(self, x):
        self.x=x
        self.next = []
    
    
def djk(node, N, K):
    
    point = [[987654321, i] for i in range(N+1)]
    lens = [987654321 for _ in range(N+1)]
    
    point[1][0]= 0
    lens[1] = 0 
    
    count = 0
    
    for length, points in node[1].next:
        
        point[points] = [length, points]
    
    point = point[1:]
    
    heapq.heapify(point)
    
    while(len(point)>0):
        
        currentLength, current = heapq.heappop(point)
        
        if(currentLength>lens[current]):
            continue
        
        for length, start in node[current].next:
            
            '''
            if(lens[start]==987654321):
                    두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있습니다.
                    -> 이 조건을 만족하는 방법은
                    1. 마을 연결도로에서 에서 최단 도로만 기록
                    2. 도로마다 계산
                    
                    구현상 편리를 위해? 2번 방식 채택
            '''
            if(True):
                newlength = length + currentLength
                
                if(lens[start]>newlength):
                    lens[start]=newlength
                    heapq.heappush(point, ([newlength, start]))
                    
    answer = filter(lambda x: (x<=K),lens[1:])
        
    return len(list(answer))
        
def solution(N, road, K):
    
    node = [nodes(i) for i in range(N+1)]
    
    for roads in (road):
        
        start, end, length = roads 
        
        
        node[start].next.append((length, end))
        node[end].next.append((length, start))
    
    return djk(node, N, K)
