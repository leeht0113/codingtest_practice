def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    min_rank = 0
    for l in lottos:
        if l in win_nums:
            min_rank += 1
    max_rank = min_rank + lottos.count(0)
    return [rank[max_rank], rank[min_rank]]