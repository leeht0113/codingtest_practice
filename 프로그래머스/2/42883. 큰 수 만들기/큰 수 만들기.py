def solution(number, k):
    collected = []
    for i, n in enumerate(number):
        while len(collected) > 0 and collected[-1] < n and k > 0:
            k -= 1
            collected.pop()
        if k == 0:
            collected.append(number[i:])
            break
        collected.append(n)

    if k > 0:
        return ''.join(number[:-k])
    return ''.join(collected)