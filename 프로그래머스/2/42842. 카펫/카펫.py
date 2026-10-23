def solution(brown, yellow):
    grid = brown + yellow
    # 카펫이 가질 수 있는 최대 크기는 3 x 3
    # 세로 길이가 3인 것부터 탐색
    for height in range(3, int(grid**0.5) + 1):
        # 나누어 떨어지지 않으면 카펫을 만들 수 없으므로 건너띔
        if grid % height != 0:
            continue
        width = grid // height
        # 현재 탐색한 카펫이 인자로 주어진 노란색 영역과 일치하면 가로, 세로 return
        if (height-2) * (width-2) == yellow:
            return [width, height]
    