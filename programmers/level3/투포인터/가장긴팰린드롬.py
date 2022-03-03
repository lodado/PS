def expand(string, left, right):
    
    while(left>=0 and right<len(string)):
        if(string[left]!=string[right]):
            break
        left-=1
        right+=1
    return len(string[left+1:right])

def solution(s):
    ans = 0
    length = len(s)
    string = s
    if(len(s)<2 or s==s[::-1]):
            return len(s)
    for i in range(0, length-1):
            ans = max(ans, expand(string,i, i+1), expand(string, i, i+2))
    return ans
