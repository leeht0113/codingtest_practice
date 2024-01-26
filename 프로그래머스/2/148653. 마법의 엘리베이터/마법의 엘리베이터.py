def solution(storey):
    answer = 0
    search = 1
    while storey > 0:
        remain = storey % (10 ** search)
        if remain > (5 * (10 ** (search - 1))):
            elevator = ((10 ** search) - remain)
            answer += (elevator // (10 ** (search-1)))
            storey += elevator
        elif remain < (5 * (10 ** (search - 1))):
            answer += (remain // (10 ** (search - 1)))
            storey -= remain
        elif remain == (5 * (10 ** (search - 1))):
            answer += (remain // (10 ** (search - 1)))
            if (storey // (10 ** (search)) % 10) >= 5:
                storey += remain
            else:
                storey -= remain
        search += 1
    return answer