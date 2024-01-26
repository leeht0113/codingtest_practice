def solution(storey):
    answer = 0
    search = 1
    while storey > 0:
        # 첫번째 자리수부터 차례대로 10 제곱의 나머지를 구함
        remain = storey % (10 ** search)
        # 나머지가 5보다 크면 큰 쪽으로 올라감
        if remain > (5 * (10 ** (search - 1))):
            elevator = ((10 ** search) - remain)
            answer += (elevator // (10 ** (search-1)))
            storey += elevator
        # 5보다 작으면 작은 쪽으로 내려감
        elif remain < (5 * (10 ** (search - 1))):
            answer += (remain // (10 ** (search - 1)))
            storey -= remain
        # 5와 같으면 그 다음 자릿 수가 5보다 크면 올라가고 작으면 내려감
        elif remain == (5 * (10 ** (search - 1))):
            answer += (remain // (10 ** (search - 1)))
            if (storey // (10 ** (search)) % 10) >= 5:
                storey += remain
            else:
                storey -= remain
        search += 1
    return answer