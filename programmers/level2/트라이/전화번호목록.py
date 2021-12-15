
class Node:
    
    def __init__(self, data):
        self.key = data
        self.data =None
        self.child = {}
        
class Trie:    
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        current = self.head

        for now in string:
            if(now not in current.child):
                current.child[now] = Node(now)            
            current = current.child[now]            
            if(current.data):
                return True
            
        current.data = string
        
        return False
           
    def search(self, string):
        current = self.head
        
        for now in string:
            if(now in current.child):
                current =  current.child[now]
            else:
                return False
        
        if(current.key):
            return True
        else:
            return False
            
        
def solution(phone_book):
    
    tr = Trie()
    pb = phone_book
    
    for i in pb:
        
        dt = tr.search(i)
        if(dt):
            return False
        else:
            if(tr.insert(i)):
                return False  
    return True
