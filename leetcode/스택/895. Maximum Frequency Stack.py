from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.cache = defaultdict(list)
        self.maxSize = 0
        
    def push(self, val: int) -> None:
        self.cnt[val]+=1
        self.cache[self.cnt[val]].append(val)
        if(self.maxSize<self.cnt[val]):
            self.maxSize = self.cnt[val]
       
    def pop(self) -> int:
        if(self.maxSize==0):
            return None
        val = self.cache[self.maxSize].pop()
        self.cnt[val]-=1
        while(self.maxSize>0 and len(self.cache[self.maxSize])==0):
            self.maxSize-=1
        return val
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
