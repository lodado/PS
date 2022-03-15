from sys import maxsize

class Solution:
    def threeSumClosest(self, arr: List[int], target: int) -> int:
        
        ans = maxsize
        answer = target
        arr.sort()
        
        for i in range(len(arr)-2):
            now = arr[i]
            left = i+1
            right = len(arr)-1
            while(left<right):
                    sums = now+arr[left]+arr[right]
                    if(sums==target):
                        return target
                    
                    if(ans>abs(target-sums)):
                        ans = min(ans, abs(target-sums))
                        answer = sums
                    if(sums>target):
                        right-=1
                    else:
                        left+=1        
        return answer
