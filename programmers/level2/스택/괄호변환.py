from sys import setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**6)

def splitIntoUV(p):
    cnt = defaultdict(int)
    
    for index, val in enumerate(p):
        cnt[val]+=1
        if(cnt['(']==cnt[')']):
            return [p[:index+1], p[index+1:]]

def isVaildBracket(p):
    st = []
    
    for i in p:
        if(i=='('):
            st.append(i)
        else:
            if(not st):
                return False
            st.pop()
    return True

def solution(inputs):
    p = inputs
    
    if(p==''):
        return p
    
    u, v = splitIntoUV(p)
    
    if(isVaildBracket(u)):
        return u+solution(v)
    else:
        ans = '(' + solution(v) + ')'
        for i in u[1:-1]:
            if(i=='('):
                ans += ')'
            else:
                ans += '('
        return ans
