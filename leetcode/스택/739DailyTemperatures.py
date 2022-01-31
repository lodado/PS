class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0 for _ in range(len(temperatures))]
        st = []
        
        for index, tmp in enumerate(temperatures):
            
            while(st and temperatures[st[-1]]<tmp):
                stackIndex = st.pop()    
                answer[stackIndex] = index - stackIndex
            st.append(index)
        return answer    
