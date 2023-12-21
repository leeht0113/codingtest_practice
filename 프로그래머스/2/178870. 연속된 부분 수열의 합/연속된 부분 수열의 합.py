def solution(sequence, k):
    answer = []
    n = len(sequence)
    interval_sum = 0
    end = 0
    for start in range(n):
        # end를 가능한 만큼 이동하기
        # 부분합이 M보다 작으면 end를 1 증가
        while interval_sum < k and end < n:
            interval_sum += sequence[end]
            end += 1
        if interval_sum == k:
            # 시간초과
            # answer.append(([start, end-1], len(sequence[start:end])))
            answer.append(([start, end-1], end-start+1))
        interval_sum -= sequence[start]
    return min(answer, key=lambda x:x[1])[0]