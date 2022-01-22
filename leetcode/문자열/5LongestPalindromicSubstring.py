class Solution:
    
    def expand(self, left, right):
        while(left>=0 and right<self.length):
            if(self.string[left]!=self.string[right]):
                break
            left-=1
            right+=1
        return self.string[left+1:right]
    
    def longestPalindrome(self, s: str) -> str:
        self.length = len(s)
        self.string = s
        
        if(len(s)<2 or s==s[::-1]):
            return s
        ans = ''
        
        for i in range(0, self.length-1):
            ans = max(ans, self.expand(i, i+1), self.expand(i, i+2), key=len)
        return ans
            
