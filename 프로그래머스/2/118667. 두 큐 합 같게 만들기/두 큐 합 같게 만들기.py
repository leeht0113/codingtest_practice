from collections import deque
def solution(queue1, queue2):
    answer = 0
    max_count = len(queue1) * 4
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    total = sum(queue1) + sum(queue2)
    # objective = total / 2
    # if any([True for q in queue1 if q > objective]) or any([True for q in queue2 if q > objective]):
    #     return -1
    # if total % 2 != 0:
    #     return -1
    while answer < max_count:
        if tot1 == tot2:
            break
        # 큰 큐에서 작은 큐로 이동
        if tot1 > tot2:
            a = queue1.popleft()
            tot1 -= a
            tot2 += a
            queue2.append(a)
        elif tot1 < tot2:
            a = queue2.popleft()
            tot2 -= a
            tot1 += a
            queue1.append(a)
        answer += 1
    if answer == max_count:
        return -1
    return answer