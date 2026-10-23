def solution(score):
    avg = []
    answer = []
    for i in score:
        avg.append(sum(i)/2)
    rank = sorted(avg, reverse=True)
    for i in avg:
        answer.append(rank.index(i)+1)
    return answer