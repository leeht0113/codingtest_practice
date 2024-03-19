from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    queue = deque()
    queue.append([begin, 0])
    visited = [0] * len(words)
    while queue:
        word, cnt = queue.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            if visited[i] == 0 and sum(x != y for x, y in zip(word, words[i])) == 1:
                queue.append([words[i], cnt + 1])
                visited[i] == 1