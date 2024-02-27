def solution(sizes):
    width = []
    height = []
    for i in range(len(sizes)):
        width.append(max(sizes[i]))
        height.append(min(sizes[i]))
    return max(width) * max(height)