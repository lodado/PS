class Solution:
    def threeSum(self, lists: List[int]) -> List[List[int]]:
        ans = []
        lists.sort()
        for ind in range(0, len(lists)):
            if(ind>0 and lists[ind]==lists[ind-1]):
                continue
            
            value = lists[ind]
            left, right = ind+1, len(lists)-1
            
            while(left<right):
                    newValue = lists[left] + lists[right] + value
                    if(newValue>0):
                        right-=1
                    elif(newValue<0):
                        left+=1
                    else:
                        ans.append([value, lists[left], lists[right]])
                        while(left<right and lists[left]==lists[left+1]):
                            left+=1    
                        while(left<right and lists[right]==lists[right-1]):
                            right-=1
                        left+=1
                        right-=1
        return ans
