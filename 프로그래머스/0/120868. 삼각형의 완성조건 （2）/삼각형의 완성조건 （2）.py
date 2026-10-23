def solution(sides):
    answer = []
    longest = max(sides)
    shortest = min(sides)
    for i in range(longest-shortest+1, longest+1):
        answer.append(i)
    for j in range(longest+1, sum(sides)):
        answer.append(j)
    return len(answer)