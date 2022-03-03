def rotate(arr):
    return zip(*arr[::-1])
    
def insertKey(newKey, background, startX, startY, size):
    for y in range(startY, startY+size):
        for x in range(startX, startX+size):
            background[y][x]+=newKey[y-startY][x-startX]
    
def removeKey(newKey, background, startX, startY, size):
    for y in range(startY, startY+size):
        for x in range(startX, startX+size):
            background[y][x]-=newKey[y-startY][x-startX]    

def isVaildKey(background, lock):
    for y in range(len(lock), len(lock)*2):
        for x in range(len(lock), len(lock)*2):
            if(background[y][x]!=1):
                return False
    return True
                   
def isAnswer(newKey, background, startX, startY, lock, size):

    insertKey(newKey, background, startX, startY, size)
    flag = isVaildKey(background, lock)
    removeKey(newKey, background, startX, startY, size)
    
    return flag
    

def solution(key, lock):
    answer = True
    
    background = [[0 for i in range(len(lock)*3)] for i in range(len(lock)*3)]
    
    for i in range(len(lock), len(lock)*2):
        for j in range(len(lock), len(lock)*2):
            background[i][j] = lock[i-len(lock)][j-len(lock)]
    
    newKey = key
    for i in range(4):
        for startY in range(0, len(lock)*2+1):
            for startX in range(0, len(lock)*2+1):
                if(isAnswer(newKey, background, startX, startY, lock, len(key))):
                        return True
        newKey = rotate(newKey)
    return False
