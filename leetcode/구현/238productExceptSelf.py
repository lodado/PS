class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        multi = 1
        
        for i in nums:
            ans.append(multi)
            multi = multi * i
        multi = 1
        
        for i in range(len(ans)-1, -1, -1):
            ans[i] = ans[i] * multi
            multi = multi * nums[i]
        return ans
