class Solution:
    def dfs(self, index, candidates, sums, arr, target):
        
        if(sums==target):
            ans.append(arr[:])
            return
        
        if(sums>target):
            return
        
        for ind in range(index, len(candidates)):
            i = candidates[ind]
            arr.append(i)
            self.dfs(ind, candidates, sums+i, arr, target)
            arr.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        global ans
        ans = []
        self.dfs(0, candidates, 0, [], target)
        
        return ans
