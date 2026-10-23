def solution(k, tangerine):
    answer = 0
    tang_dict = {}
    count = 0
    for t in tangerine:
        tang_dict[t] = tang_dict.get(t, 0) + 1
    arr = sorted(tang_dict.items(), key=lambda x: x[1], reverse=True)
    if arr[0][1] >= k:
        return 1
    else:
        for key, value in arr:
            if count < k:
                count += value
                answer += 1
            else:
                break
    return answer