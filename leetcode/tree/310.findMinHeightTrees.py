from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = defaultdict(list)
        
        if(n==1):
            return [0]
        
        for start, end in edges:
            nodes[start].append(end)
            nodes[end].append(start)
        
        leaves = []
        
        for i in range(n+1):
            if(len(nodes[i])==1):
                leaves.append(i)
                
        while(n>2):
            n -= len(leaves)
            lv = []
            
            for i in leaves:
                end = nodes[i].pop()
                nodes[end].remove(i)
                if(len(nodes[end])==1):
                    lv.append(end)
            leaves = lv
        
        return leaves
