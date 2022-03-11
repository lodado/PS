from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        dic = defaultdict(list)
        index = 0
        down = 1
        up = -1 
        
        move = 0
        
        for character in s:
            if index == 0:
                move = down
            elif index == numRows - 1: 
                move = up
                
            dic[index].append(character)
            index+=move
            
        string = ''
        for v in dic.values():
            string += ''.join(v)
        
        return string
