def solution(s):
    data = s[2:-2].split("},{")
    data = sorted(data, key=lambda x: len(x))
    answer = []
    for item in data:
        # 쪼갠 문자열을 한 번더 ','를 기준으로 쪼갬
        # 중괄호를 제거한 숫자 문자열 -> 문자열을 숫자로 변환 -> 숫자
        item = list(map(int, item.split(',')))
        for value in item:
            # 중복을 확인하면서 루프를 진행
            if value not in answer:
                answer.append(value)
    return answer