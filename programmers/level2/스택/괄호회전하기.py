from collections import Counter

hsh = {'{':'}', '[':']', '(':')'}

def isVaildBracket(s):
    global hsh
    st = []
    
    for val in s:
        if val in '{[(':
            st.append(val)
        elif(st and hsh[st[-1]]==val):
            st.pop()
        else:
            return False
    if(st):
        return False
    return True
        
def getAnswer(s):
    string = s
    answer = 0
    for i in range(len(s)):
        if(isVaildBracket(string)):
            answer+=1
        string = string[1:] + string[0] 
    return answer
    
def isVaildString(s):
    global hsh
    cnt = Counter(s)
    
    for k, v in hsh.items():
        if(cnt[k]!=cnt[v]):
            return False
    return True
    

def solution(s):
    if not(isVaildString(s)):
        return 0
    return getAnswer(s)
