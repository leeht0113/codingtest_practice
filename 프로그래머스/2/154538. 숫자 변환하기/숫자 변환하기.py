# from collections import deque

# def solution(x, y, n):
#     answer = 0
#     visited = [0] * (y+1)
#     move = [n, 2, 3]

#     if x== y:
#         return 0

#     queue = deque()
#     queue.append(x)
#     while queue:
#         start = queue.popleft()
#         for i in range(len(move)):
#             if i == 0:
#                 loc = start + move[i]
#             else:
#                 loc = start * move[i]
#             if loc <= y and visited[loc] == 0:
#                 queue.append(loc)
#                 visited[loc] = visited[start] + 1
#     answer = visited[-1]
#     if answer:
#         return answer
#     else:
#         return -1

def solution(x, y, n):
    answer = 0
    dp = set()
    dp.add(x)

    while dp:
        if y in dp:
            return answer
        else:
            dp_y = set()
            for i in dp:
                if i+n <= y:
                    dp_y.add(i+n)
                if i*2 <= y:
                    dp_y.add(i*2)
                if i*3 <= y:
                    dp_y.add(i*3)
            dp = dp_y
            answer += 1

    return -1