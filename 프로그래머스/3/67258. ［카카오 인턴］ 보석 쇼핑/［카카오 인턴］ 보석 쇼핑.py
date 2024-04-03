def solution(gems):
    answer = []
    n = len(set(gems))
    length = len(gems)
    gems_dict = {}
    shortest_length = len(gems) + 1
    lt = 0
    for rt in range(length):
        curr_rt = gems[rt]
        gems_dict[curr_rt] = gems_dict.get(curr_rt, 0) + 1
        while len(gems_dict) == n:
            # print((lt, rt), gems_dict, shortest_length)
            if (rt - lt + 1) < shortest_length:
                # print(shortest_length)
                shortest_length = (rt - lt + 1)
                answer = [lt + 1, rt + 1]
            curr_left = gems[lt]
            if gems_dict[curr_left] == 1:
                del gems_dict[curr_left]
            else:
                gems_dict[curr_left] -= 1
            lt += 1
    return answer
