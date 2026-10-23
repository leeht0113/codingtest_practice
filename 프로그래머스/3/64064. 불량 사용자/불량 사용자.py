import re
from itertools import permutations

def solution(user_id, banned_id):
    match = set()
    patterns = [b.replace('*', '.') for b in banned_id]
    for p in patterns:
        for u in user_id:
            if re.fullmatch(p,u):
                match.add(u)
    match = list(match)
    n = len(patterns)
    answer = []
    for i in permutations(match, n):
        comb = list(i)
        flag = True
        for j in range(n):
            if re.fullmatch(patterns[j], comb[j]):
                continue
            else:
                flag = False
                break
        if flag:
            sorted_comb = sorted(comb)
            if sorted_comb not in answer:
                answer.append(sorted_comb)
    return len(answer)
    
        
        