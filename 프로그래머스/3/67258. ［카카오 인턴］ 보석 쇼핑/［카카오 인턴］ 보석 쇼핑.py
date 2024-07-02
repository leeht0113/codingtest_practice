def solution(gems):
    gems_type = len(set(gems))
    if gems_type == 1:
        return [1, 1]
    answer = []
    start = 0
    length = len(gems)
    shortest_length = len(gems) + 1
    gems_dict = {}
    for end in range(length):
        curr_end = gems[end]
        gems_dict[curr_end] = gems_dict.get(curr_end, 0) + 1
        while start < end and len(gems_dict) == gems_type:
            curr_length = (end - start) + 1
            if curr_length < shortest_length:
                shortest_length = curr_length
                answer = [start + 1, end + 1]
            curr_start = gems[start]
            gems_dict[curr_start] -= 1
            if gems_dict[curr_start] == 0:
                del gems_dict[curr_start]
            start += 1
    return answer