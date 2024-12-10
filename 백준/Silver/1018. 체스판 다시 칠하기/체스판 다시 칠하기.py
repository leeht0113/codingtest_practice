m, n = map(int, input().split())

chess = [input() for _ in range(m)]

answer = float("inf")

def fill(i, j, color, answer):
    count = 0
    for x in range(i, i + 8):
        for y in range(j, j + 8):
            if color != chess[x][y]:
                count += 1
            # B 다음에는 W가 와야 됨
            if color == "B" and y != j + 7:
                color = "W"
            # W 다음에는 B가 와야 됨
            elif color == "W" and y != j + 7:
                color = "B"
    answer = min(count, answer)
    return answer

for i in range(0,  m - 7):
    for j in range(0, n - 7):
        answer = fill(i, j, "W", answer)
        answer = fill(i, j, "B", answer)

print(answer)