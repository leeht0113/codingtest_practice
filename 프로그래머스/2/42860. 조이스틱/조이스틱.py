def solution(name):
    answer = 0
    min_move = len(name) - 1
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        n = i + 1
        while n < len(name) and name[n] == 'A':
            n += 1
        min_move = min([min_move, 2 * i + len(name) - n, i + 2 *(len(name) - n)])
    answer += min_move
    return answer