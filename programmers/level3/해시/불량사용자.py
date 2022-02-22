from itertools import permutations 
import re

def check(users, banned_id):
    for user, ban_id in zip(users, banned_id): 
            if not re.match(ban_id, user):
                return False
    return True
    
def solution(user_id, banned_id):
    answer = 0
    user_permutation = list(permutations(user_id,len(banned_id)))
    
    ans = []
    banned_id = [(i.replace('*', '.')+'$') for i in banned_id]
        
    for users in user_permutation:
        if(check(users, banned_id)):
            usersSet = set(users)
            if(usersSet not in ans):
                ans.append(usersSet)
    
    return len(ans)
