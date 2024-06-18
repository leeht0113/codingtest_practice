def solution(elements):
    answer = set()
    elements = elements * 2
    # print(elements)
    sum_value = 0
    prefix_sum = [0]
    for e in elements:
        sum_value += e
        prefix_sum.append(sum_value)
    # print(prefix_sum)
    for i in range(1, (len(prefix_sum)//2)+ 1):
        temp = []
        for j in range(1, len(elements) + 1):
            if i + j <= len(elements) - 1:
                # print(i, j)
                temp.append(prefix_sum[i + j] - prefix_sum[j])
        # print(set(temp))
        answer.update(set(temp))
    # print(answer)
    return len(answer)