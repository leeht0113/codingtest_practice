from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        temp = deque(skill)
        
        for s in skills:
            if s in temp and s != temp.popleft():
                break
        else:
            answer += 1        
            
    return answer