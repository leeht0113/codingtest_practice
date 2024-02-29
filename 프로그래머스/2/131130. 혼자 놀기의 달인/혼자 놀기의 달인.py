def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(cards):
    group = {}
    answer = 1
    v = len(cards)
    parent = [0] * (v + 1)
    for i in range(1, v + 1):
        parent[i] = i
    for i in range(1, v + 1):
        union_parent(parent, i, cards[i-1])
    for i in range(1, v + 1):
        find_parent(parent, i)
    for i in parent[1:]:
        group[i] = group.get(i, 0) + 1
    group = sorted(group.values(), reverse=True)
    if len(group) > 1:
        for g in group[:2]:
            answer *= g
        return answer
    else:
        return 0