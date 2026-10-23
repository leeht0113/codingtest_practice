def solution(new_id):
    # 1. 모든 대문자를 대응되는 소문자로 치환
    answer = new_id.lower()
    # 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    filtered = []
    for c in answer:
        if c.isalpha() or c.isdigit() or c in ['-','_','.']:
            filtered.append(c)
    answer = ''.join(filtered)
    # 3. 마침표(.) 2번 이상 반복되면 하나의 마침표(.)로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4. 마침표(.)가 처음이나 끝에 위치한다면 제거
    answer = answer.strip('.')
    # 5. 빈 문자열이라면, "a"를 대입
    if len(answer) == 0:
        answer = "a"
    # 6. 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자들은 제거
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer.rstrip('.')
    # 7. 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    return answer