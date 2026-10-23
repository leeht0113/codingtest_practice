def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer