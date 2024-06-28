n, m = map(int, input().split())
result = []
visited = [False] * (n + 1)

def recursive(num):
    if num == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            recursive(num+1)
            visited[i] = False
            result.pop()

recursive(0)