from sys import setrecursionlimit
setrecursionlimit(10**9)

class Node:
    def __init__(self, index, name):
        self.index = 0
        self.name = name
        self.money = 0
        self.parent = None
        self.children = []
    
    def insertChildren(self, node):
        self.children.append(node)
    
    def getMoney(self, money):
        
        tax = int(money * (1/10))        
        self.money += money - tax
        if(tax>0):
            self.giveMoney(tax)
        
    def giveMoney(self, money):
        if(self.parent):
            self.parent.getMoney(money)
        
def solution(enroll, referral, seller, amount):
    
    nodes = {}
    person = [Node(index, name) for index, name in enumerate(enroll)]
    for index, p in enumerate(person):
        nodes[p.name] = p
    
    for index, ref in enumerate(referral):
        if(ref!='-'):
            nodes[ref].insertChildren(person[index])
            person[index].parent = nodes[ref]
    
    for sell, money in zip(seller, amount):
        nodes[sell].getMoney(money*100)
        
    answer = [i.money for i in person]
    return answer
