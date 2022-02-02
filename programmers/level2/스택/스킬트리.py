def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        flag = True
        index = 0
        for val in skill_tree:
            if(val in skill):
                if(skill[index]==val):
                    index+=1
                else:
                    flag=False
                    break
        if(flag):
            answer+=1
    return answer
