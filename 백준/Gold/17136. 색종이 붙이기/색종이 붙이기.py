board = [list(map(int, input().split())) for _ in range(10)]
ans = 25
paper = [0] * 6

def is_possible(y, x, sz):
    if paper[sz] == 5: # 색종이 개수 체크
        return False 
    if y + sz > 10 or x + sz > 10: # 범위 체크
        return False
    # size 만큼 다 1로 이루어져 있는지 검사
    for i in range(sz):
        for j in range(sz):
            if board[y + i][x + j] == 0:
                return False
    return True

def mark(y, x, sz, v):
    for i in range(sz):
        for j in range(sz):
            board[y + i][x + j] = v
    if v: # 원상복구, 색종이를 다시 뗌
        paper[sz] -= 1
    else: # 0이면 색종이를 사용
        paper[sz] += 1

def backtracking(y, x):
    global ans
    if y == 10: # 하나의 경우가 완성됨
        ans = min(ans, sum(paper))
        return 
    
    if x == 10: # 다음줄로 넘어감
        backtracking(y + 1, 0)
        return
    
    if board[y][x] == 0: # 현재 칸이 0인 경우에는 바로 다음 칸을 보면 됨
        backtracking(y, x + 1)
        return
    # board[y][x]가 1인 경우에만 옴
    # 색종이 사이즈 1부터 5까지 전부다 대 보고 가능하면 색종이를 실제로 덮음
    for sz in range(1, 6):
        if is_possible(y, x, sz): # y, x를 만났을 때 y, x를 좌상단으로 갖는 정사각형의 사이즈만큼 다 1로 이루어져 있는지 검사
            mark(y, x, sz, 0) # 색종이를 덮음 (size 크기 만큼의 정사각형 1들을 다 0으로 marking하는 함수)
            backtracking(y, x + 1)
            mark(y, x, sz, 1) # 원상복구

backtracking(0, 0)
print(-1 if ans == 25 else ans)