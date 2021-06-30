class node:
    def __init__(self, x):
        self.x= x
        self.next = []

def dfs(now, coms, check, visited):

    visited[now]=True

    for i in coms[now].next:
        if(visited[i]==False):
            check[i]=check[now]
            dfs(i, coms, check, visited)



def solution(n, computers):
    answer = 0

    coms = [node(i) for i in range(len(computers)+1)]

    for index, i in enumerate(computers):
        index = index+1
        for index2, j in enumerate(i):
            index2 = index2 + 1

            if(j==1 and index!=index2):
                coms[index].next.append(index2)
                coms[index2].next.append(index)            

    for i in coms[1:]:
        print(i.x)
        print(i.next)

    check = [-1 for _ in range(len(computers)+1)]
    visited = [False for _ in range(len(computers)+1)]

    count=0

    for i in range(1,len(computers)+1):
        if(visited[i]==False):
            count+=1
            check[i]=i
            dfs(i, coms, check, visited)

    return count