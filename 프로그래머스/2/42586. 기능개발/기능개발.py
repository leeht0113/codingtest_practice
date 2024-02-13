from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        p = progresses[0]
        if p >= 100:
            cnt = 1
            progresses.popleft()
            speeds.popleft()
            while progresses and progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                cnt += 1
            answer.append(cnt)
    return answer