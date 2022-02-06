class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        used = {}
        left = 0
        answer = 0
        
        for index, char in enumerate(s):
            
            if char in used and left<=used[char]:
                left = used[char]+1
            else:
                answer = max(answer, index-left+1)
            used[char] = index
                    
        return answer
