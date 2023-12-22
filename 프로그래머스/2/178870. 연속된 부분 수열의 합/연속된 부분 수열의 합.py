def solution(sequence, k):
    answer = []
    n = len(sequence)
    interval_sum = 0 # 구간합
    end = 0
    for start in range(n):
        # end를 가능한 만큼 이동하기
        # 부분합이 k보다 작으면 end를 1 증가
        while interval_sum < k and end < n:
            interval_sum += sequence[end]
            end += 1
        if interval_sum == k:
            # 시간초과
            # answer.append(([start, end-1], len(sequence[start:end])))
            answer.append(([start, end-1], end-start+1))
        # 현재 부분 합이 k보다 작다면, end를 1 증가시킨다
        interval_sum -= sequence[start]
    return min(answer, key=lambda x:x[1])[0]