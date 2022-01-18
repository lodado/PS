def solution(id_list, report, k):
    answer = []
    dic = dict()
    rex = dict()
    
    for i in id_list:
        dic[i] = []
        rex[i] = 0
    
    for rep in report:
        reporter, reported = rep.split(' ')
        if(reporter not in dic[reported]):
            dic[reported].append(reporter)
    
    for key, v in dic.items():
        if(len(v)>=(k)):
            for ind in v:
                rex[ind]+=1
                continue        
                
    for v in rex.values():
        answer.append(v)

    return answer
