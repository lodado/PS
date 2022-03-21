from sys import maxsize

class Solution:
    def merge(self, inputs: List[List[int]]) -> List[List[int]]:
        ans = []
        
        if not(inputs):
            return []
        
        intervals = inputs[:]
        intervals.sort(key=lambda x:x[0])
        left, right = intervals[0]
        intervals.append([maxsize, maxsize])
        
        for start, end in intervals:
            if(start>right):
                ans.append([left, right])
                left, right = start, end 
            else:
                if(right<end):
                    right = end
        return ans
