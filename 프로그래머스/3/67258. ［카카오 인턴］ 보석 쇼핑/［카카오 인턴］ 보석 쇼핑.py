def solution(gems):
    gem_types = len(set(gems))  # 고유 보석 종류의 수
    gem_dict = {}  # 현재 창에 있는 보석과 그 개수를 저장하는 딕셔너리
    start, end = 0, 0  # 슬라이딩 윈도우의 시작과 끝 인덱스
    answer = [0, len(gems) - 1]  # 초기 구간을 최대로 설정
    shortest = len(gems) + 1  # 찾을 구간의 길이

    while end < len(gems):
        # 현재 보석을 추가
        if gems[end] not in gem_dict:
            gem_dict[gems[end]] = 1
        else:
            gem_dict[gems[end]] += 1

        # 모든 종류의 보석이 창에 있을 때, 시작 지점을 최대한 오른쪽으로 이동
        while len(gem_dict) == gem_types:
            if end - start < shortest:
                shortest = end - start
                answer = [start + 1, end + 1]  # 1-based index

            if gem_dict[gems[start]] == 1:
                del gem_dict[gems[start]]
            else:
                gem_dict[gems[start]] -= 1
            start += 1

        end += 1

    return answer
