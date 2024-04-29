def solution(order):
    l = len(order)
    idx = 0 # 실어야되는 상자
    num = 0 # 메인 컨테이너에 있는 상자
    aux_container = []
    while idx < l:
        # 현재 컨테이너에 있는 상자보다 실어야되는 상자보다 번호가 작으면
        if order[idx] > num:
            # 보조 컨테이너에 적재
            num += 1
            aux_container.append(num)
            # if idx < l:
            #     print('보조 컨테이너에 적재', aux_container, order[idx], num)
        # 현재 컨테이너에 있는 상자가 보조 컨테이너의 마지막 상자와 같으면
        elif order[idx] == aux_container[-1]:
            # 보조 컨테이너 벨트에서 빼옴, 메인 컨테이너에는 상자 안 뺌
            idx += 1
            aux_container.pop()
            # if idx < l:
                # print('보조 컨테이너 벨트에서 빼옴', aux_container, order[idx], num)
        else:
            # print('더 이상 실을 수 있는 상자가 없음', aux_container, order[idx], num)
            return idx
    return idx