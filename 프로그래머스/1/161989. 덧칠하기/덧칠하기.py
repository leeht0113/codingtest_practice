def solution(n, m, section):
    cnt, k = 0, 0
    for s in section:
        # 페인트 칠이 끝나는 지점인 k보다 칠해야할 구역의 번호가 크면 다시 그 시점부터 페인트 칠 시작
        if s > k:
            cnt += 1
            k = s + (m-1) # 페인트 칠 끝나는 위치 재지정
    return cnt