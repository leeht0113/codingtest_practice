def solution(d, budget):
    d.sort()
    for i, cost in enumerate(d):
        budget -= cost
        if budget < 0:
            return i
    return len(d)