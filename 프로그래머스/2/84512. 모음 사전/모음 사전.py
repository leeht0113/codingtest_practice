def find(data, vowel, cnt):
    if cnt == 6:
        return
    if vowel != '':
        data.append(vowel)
    for v in ['A', 'E', 'I', 'O', 'U']:
        find(data, ''.join([vowel, v]), cnt + 1)

def solution(word):
    answer = 0
    data = []
    find(data, '', 0)
    for i in range(len(data)):
        if data[i] == word:
            answer = i + 1
    return answer