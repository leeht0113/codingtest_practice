from collections import deque

def solution(board):
    size = len(board)
    # 상/좌/하/우
    paths = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    # BFS 함수를 구현
    # BFS 함수가 여러 번 실행되어야 하므로 따로 함수를 분리하여 만듦
    
    def bfs(x, y, cost, path):
        # 방문 배열
        graph = [[0] * size for _ in range(size)]
        for a in range(size):
            for b in range(size):
                if board[a][b] == 1: graph[a][b] = -1
                
        q = deque()
        q.append((x, y, cost, path))
        
        while q:
            x, y, cost, path = q.popleft()
            
            for i in range(len(paths)):
                nx = x + paths[i][0]
                ny = y + paths[i][1]
                
                if nx < 0 or nx >= size or ny < 0 or ny >= size or graph[nx][ny] == -1:
                    continue
                # 직선도로이면 100원 추가
                if path == i:
                    newcost = cost + 100
                # 코너이면 500원 추가
                else:
                    newcost = cost + 600
                # 도면의 상태가 비어 있거나 방문 배열의 값이 새로운 값보다 크면 큐에 데이터를 추가
                if graph[nx][ny] == 0 or (graph[nx][ny] != 0 and graph[nx][ny] > newcost):
                    q.append((nx, ny, newcost, i))
                    graph[nx][ny] = newcost
        return graph[size - 1][size - 1]
                
    return min(bfs(0, 0, 0, 2), bfs(0, 0, 0, 3))
