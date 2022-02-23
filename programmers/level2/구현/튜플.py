import re

def solution(s):
    answer = []
    
    arr = s.lstrip('{').rstrip('}').split("},{")
    numArrayContainer = [list(map(int, string.split(',')))  for string in arr]
    
    numArrayContainer.sort(key=lambda x:len(x))
    
    for numArray in numArrayContainer:
        for num in numArray:
                if(num not in answer):
                    answer.append(num)
    return answer
