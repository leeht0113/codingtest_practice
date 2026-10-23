def solution(s):
    s = list(s)
    cnt = 0
    for i in range(len(s)):
        if s[i] == ' ':
            cnt = 0
            continue
        cnt += 1
        s[i] = s[i].upper() if cnt % 2 == 1 else s[i].lower()
    return ''.join(s)