def solution(array):
    keys = set(array)
    dict_ = {}
    max_count = []
    for i in keys:
        dict_[i] = array.count(i)
    for i in keys:
        if dict_[i] == max(dict_.values()):
            max_count.append(i)
    if len(max_count) > 1:
        return -1
    else:
        return max_count[0]