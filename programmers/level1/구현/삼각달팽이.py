def solution(n):
    answer = [[0 for _ in range(i+1)] for i in range(n)]
    x, y = 0, -1
    number = 1
    
    for i in range(n):
        for j in range(i, n):
            if(i%3==0):
                y+=1
            elif(i%3==1):
                x+=1
            else:
                y-=1
                x-=1
            answer[y][x] = number
            number+=1
    
    return sum(answer, [])
