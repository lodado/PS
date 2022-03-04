def solution(board, skill):
    answer = 0
    newBoard = [[0 for j in range(len(board[0])+1)] for i in range(len(board)+1)]
    
    for t, y1, x1, y2, x2, degree in skill:
        if(t==2):
            newBoard[y1][x1] += degree
            newBoard[y1][x2+1] -= degree
            newBoard[y2+1][x1] -= degree
            newBoard[y2+1][x2+1] += degree
        else:
            newBoard[y1][x1] -= degree
            newBoard[y1][x2+1] += degree
            newBoard[y2+1][x1] += degree
            newBoard[y2+1][x2+1] -= degree
    
    for y in range(len(newBoard)):
        now = 0
        for x in range(len(newBoard[0])):
            now += newBoard[y][x]
            newBoard[y][x]=now
            
    for x in range(len(newBoard[0])):
        now = 0
        for y in range(len(newBoard)):
            now += newBoard[y][x]
            newBoard[y][x]=now        
    
    for y in range(len(board)):
        for x in range(len(board[0])): 
            if(board[y][x]+newBoard[y][x]>0):
                answer+=1
    
    return answer
