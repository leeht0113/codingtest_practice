from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    weak.extend([w + n for w in weak])
    answer = len(dist) + 1
    for i in range(length):
        for f in permutations(dist, len(dist)):
            cnt = 1
            position = weak[i] + f[cnt - 1]
            for j in range(i + 1, i + length):
                if position < weak[j]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    position = weak[j] + f[cnt - 1]
            answer = min(answer, cnt)
    return answer if answer <= len(dist) else -1