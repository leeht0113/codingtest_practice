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

def solution(n, costs):
    answer = 0
    cnt = 0
    edges = []
    parent = [0] * n
    
    for i in range(1, n):
        parent[i] = i
        
    for c in costs:
        a, b, cost = c
        edges.append((cost, a, b))
        
    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
            cnt += 1
        if cnt == (n - 1):
            break
            
    return answer