import re
import copy
from collections import deque

def solution(begin, target, wordsParam):

    words = copy.deepcopy(wordsParam)
    deq = deque([[begin, 0]])
    
    while(deq):
        word, count = deq.popleft()
        
        if(word==target):
            return count
        
        for index in range(0, len(word)):
            startWord = word[:index]
            endWord = word[index+1:]
            saveArr = []
            
            for otherWord in words:
                if(otherWord!=word):
                    if(re.match('{}\w{}'.format(startWord,endWord), otherWord)):
                        deq.append([otherWord, count+1])
                    else:
                        saveArr.append(otherWord)
            words = saveArr
    return 0
