def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma" ]
    for i in babbling:
        for s in word:
            i = i.replace(s, "!", 1) # 발음 존재시 !로 치환, 1번만 바꿈
        if i.replace('!', '') == '': # 치환된 문자열을 ''로 다시 치환하여 공백이면 발음 가능함
            answer += 1
    return answer