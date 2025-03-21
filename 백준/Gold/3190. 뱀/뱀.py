from collections import deque

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수
apple_loc = [] # 사과의 위치
for _ in range(k):
    apple_loc.append(list(map(int, input().split())))
l = int(input())
snake_change = [] # 뱀의 방향 변환 횟수
for _ in range(l):
    snake_change.append(input().split())
board = [[0] * n for _ in range(n)]
for a in apple_loc:
    a_r, a_c = a
    board[a_r-1][a_c-1] = 1
dx = [1, 0, -1, 0] # 동, 남, 서, 북
dy = [0, 1, 0, -1]
second = 0
board[0][0] = 2
change = deque(snake_change)
loc = deque([[0, 0]])
tail = deque([[0, 0]])
direction = 0
while True:
    second += 1
    prev_x, prev_y = loc.popleft()
    new_x, new_y = prev_x + dx[direction], prev_y + dy[direction]
    # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
        break
    elif board[new_y][new_x] == 2: 
        break
    # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if board[new_y][new_x] == 1:
        board[new_y][new_x] = 2
    # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    elif board[new_y][new_x] == 0: 
        board[new_y][new_x] = 2
        apple_x, apple_y = tail.popleft() # 꼬리 위치
        board[apple_y][apple_x] = 0
    if len(change) > 0:
        change_second, change_direction = change[0]
        change_second = int(change_second)
        if second == change_second:
            if change_direction == 'L':
                direction = (direction - 1) % 4
            elif change_direction == 'D':
                direction = (direction + 1) % 4
            change.popleft()
    loc.append([new_x, new_y])
    tail.append([new_x, new_y])
print(second)