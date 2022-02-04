from itertools import product

def solution(word):
    return sorted(sum([list(map(''.join, (product('AEIOU', repeat=i)))) for i in range(1, 6)], [])).index(word)+1
