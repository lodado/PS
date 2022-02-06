from collections import defaultdict

def matchingStrings(strings, queries):
    dic = defaultdict(int)
    
    for string in strings:
        dic[string]+=1
    
    return [dic[query] for query in queries]
