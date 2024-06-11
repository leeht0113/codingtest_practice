def solution(n, s, a, b, fares):
    INF = float("inf")
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0
                
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    answer = INF
    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
        
    return answer