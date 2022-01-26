from itertools import permutations
import math

def solution(numbers):
    answer = 0
    
    lists = list(map(int, numbers))
    arr = [True for _ in range(int('9'*7)+1)]
    length = int(math.sqrt(len(arr)))+1
    
    arr[0], arr[1] = False, False
    
    for i in range(2, length):
        if(arr[i]):
            for j in range(i*2, len(arr), i):
                arr[j] = False
                
    for length in range(1, len(numbers)+1):
        for i in permutations(lists, length):
            
            num = int(''.join(map(str, i)))
            
            if(arr[num]):
                arr[num]= False
                answer+=1
    
    return answer
