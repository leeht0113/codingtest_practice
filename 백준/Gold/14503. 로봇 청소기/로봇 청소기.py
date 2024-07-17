n, m = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
count = 0
# 북, 동, 남, 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while True:
    if map[y][x] == 0:
        map[y][x] = 2
        count += 1
    flag = False
    for i in range(1, 5):
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        if 0<=ny<n and 0<=nx<m:
            if map[ny][nx] == 0:
                # 바라보는 방향을 기준으로
                # 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다. 1번으로 돌아간다
                d = (d - i + 4) % 4
                y = ny
                x = nx
                flag = True # 청소를 한 경우
                break
    # 4방향 모두 있지 않은 경우
    if flag == False:
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        # 뒤쪽 방향이 막혀있는지 확인
        ny = y - dy[d]
        nx = x - dx[d]
        if 0 <= ny < n and 0<= nx < m:
            if map[ny][nx] == 1:
                break
            else:
                y = ny
                x = nx
        else:
            break

print(count)