from collections import defaultdict

def dfs(graph, path, visit):
    if path:
        to = path[-1]
        if graph[to]:
            path.append(graph[to].pop())
        else:
            visit.append(path.pop())
        dfs(graph, path, visit)
    return visit[::-1]

def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    for key in graph:
        graph[key].sort(reverse=True)
    # print(graph)
    return dfs(graph, ["ICN"], [])