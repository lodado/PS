def push(que, newValue):
    if(que and que[-1]==newValue):
        que.pop()
        return 2
    else:
        que.append(newValue)
        return 0

def solution(board, moves):
    answer = 0
    que = []
    length = len(board)
    
    for locate in moves:
        row = locate - 1 
        for col in range(length):
            if(board[col][row]!=0):
                answer+=push(que, board[col][row])
                board[col][row] = 0
                break 
    return answer
