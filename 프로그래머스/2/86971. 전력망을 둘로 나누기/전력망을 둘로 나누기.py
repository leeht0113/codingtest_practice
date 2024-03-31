cnt = 0

def dfs(v, visited, graph):
    global cnt
    visited[v] = 1
    cnt += 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i, visited, graph)
    # print(v, visited)
    
def solution(n, wires):
    global cnt
    answer = n
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    for a, b in wires:
        cnt = 0
        visited = [0] * (n + 1)
        visited[b] = 1
        dfs(a, visited, graph)
        # print(a, visited, cnt, abs((n - cnt) - (cnt)))
        answer = min(answer, abs(n - 2 * cnt))
    return answer