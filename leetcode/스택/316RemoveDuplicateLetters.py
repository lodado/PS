from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        cnt, stack = Counter(s), []
        for val in s:
            cnt[val]-=1    
            if val in stack:
                continue

            while(stack and val<stack[-1] and cnt[stack[-1]]>0):
                stack.pop()
            stack.append(val)
            
        return ''.join(stack)  
