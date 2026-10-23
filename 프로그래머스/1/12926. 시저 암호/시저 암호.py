def solution(s, n):
    answer = []
    for i in s:
        if i == ' ':
            answer.append(' ')
            continue
        if i.isupper():
            start = ord('A')
        else:
            start = ord('a')
        diff = (ord(i) - start) + n
        answer.append(chr(start + (diff)%26))
    return ''.join(answer)