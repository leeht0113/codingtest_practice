from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    people = defaultdict(list)
    
    for i in info:
        person = i.split()
        score = int(person.pop())
        people[''.join(person)].append(score)
        for j in range(4):
            combi = list(combinations(person, j))
            for c in combi:
                people[''.join(c)].append(score)
                
    for p in people:
        people[p].sort()
        
    for q in query:
        key = q.split()
        score = int(key.pop())
        key = ''.join(key).replace('and', '').replace('-', '')
        left = 0
        right = len(people[key])
        scores = people[key]
        while left < right:
            mid = (left + right) // 2
            if scores[mid] < score:
                left = mid + 1
            elif scores[mid] >= score:
                right = mid
        answer.append(len(people[key]) - left)
        
    return answer