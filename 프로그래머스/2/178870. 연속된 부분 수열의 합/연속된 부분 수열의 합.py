def solution(sequence, k):
    answer = []
    n = len(sequence)
    interval_sum = 0
    end = 0
    for start in range(n):
        while interval_sum < k and end < n:
            interval_sum += sequence[end]
            end += 1
        if interval_sum == k:
            answer.append(([start, end - 1], end - start))
        interval_sum -= sequence[start]
    return min(answer, key = lambda x:x[1])[0]