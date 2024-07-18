n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        answer += 1
    flag = False
    for i in range(1, 5):
        new_d = (d - i + 4) % 4
        nr = r + dr[new_d]
        nc = c + dc[new_d]
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0:
            flag = True
            r = nr
            c = nc
            d = new_d
            break
    if not flag:
        nr = r - dr[d]
        nc = c - dc[d]
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] != 1:
            r = nr
            c = nc
        else:
            break
print(answer)