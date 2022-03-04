import re

def sort(inputs):
    
    return [inputs[0].upper(), int(inputs[1])]

def solution(files):
    lists = []
    answer = []
    
    for file in files:
        num = re.search('([^0-9]+)(\d+)(.+)?', file)
        lists.append(num.groups())
    lists.sort(key=sort)
    
    for head, number, tail in lists:
        string = head+number
        if(tail):
            string+=tail
        answer.append(string)    
    
    return answer
