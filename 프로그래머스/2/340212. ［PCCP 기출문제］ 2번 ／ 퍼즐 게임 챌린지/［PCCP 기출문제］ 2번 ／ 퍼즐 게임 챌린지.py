def solution(diffs, times, limit):
    start = 1
    end = max(diffs)
    length = len(diffs)
    while start < end:
        level = (start + end) // 2
        total = times[0]
        for i in range(1, length):
            if diffs[i] <= level:
                total += times[i]
            else:
                total += ((diffs[i] - level) * (times[i] + times[i - 1])) + times[i]
        if total <= limit:
            end = level
        else:
            start = level + 1
    return start