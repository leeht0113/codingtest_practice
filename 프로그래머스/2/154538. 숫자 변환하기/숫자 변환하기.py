from collections import deque

def solution(x, y, n):
    answer = 0
    calc = [n, 2, 3]
    visited = [0] * (y + 1)
    queue = deque()
    queue.append(x)
    # visited[x] = 1
    if x == y:
        return 0
    while queue:
        start = queue.popleft()
        # print(start)
        # print(visited[start])
        for i in range(len(calc)):
            if i == 0:
                new_number = start + calc[i]
                if start <= new_number <= y and visited[new_number] == 0:
                    visited[new_number] = visited[start] + 1
                    queue.append(new_number)
                    if new_number == y:
                        # print(visited)
                        return visited[y]
            elif i == 1:
                new_number = start * calc[i]
                if start <= new_number <= y and visited[new_number] == 0:
                    visited[new_number] = visited[start] + 1
                    queue.append(new_number)
                    if new_number == y:
                        # print(visited)
                        return visited[y]
            elif i == 2:
                new_number = start * calc[i]       
                if start <= new_number <= y and visited[new_number] == 0:
                    visited[new_number] = visited[start] + 1
                    queue.append(new_number)
                    if new_number == y:
                        return visited[y]
    # print(visited)
    if visited[y] != 0:
        return visited[y]
    else:
        return -1