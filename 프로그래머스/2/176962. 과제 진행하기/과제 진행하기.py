def solution(plans):
    answer = []
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        total = h * 60 + m
        plans[i][1] = total
        plans[i][2] = int(plans[i][2])
    plans.sort(key = lambda x: x[1])
    # print(plans)
    subject = []
    for i in range(len(plans)):
        # 마지막 수업인 경우 잠시 멈춰둔 과제 배열에 저장하고 break
        if i == len(plans) - 1:
            subject.append(plans[i])
            break
        # 현재 과제에 대한 정보
        cur_subject, start, playtime = plans[i]
        # 다음 과제에 대한 정보
        n_subject, n_start, n_playtime = plans[i + 1]
        # 현재 과제가 끝나는 예정 시간이 다음 과제의 시작 시간보다 작으면 정답 배열에 담음
        if start + playtime <= n_start:
            answer.append(cur_subject)
            remain_time = n_start - (start + playtime) # 남은 시간 기록
            # 남은 시간이 0이 아니고 멈춰둔 과제가 있다면 멈춰둔 과제를 진행
            # 남은 시간이 0이 될 때가지 진행
            while remain_time != 0 and subject:
                stop_subject, stop_start, stop_playtime = subject.pop()
                # 과제를 마치는 데 걸리는 시간이 남은 시간보다 작으면 정답 배열에 담음
                # 남은 시간에서 과제를 마치는 걸리는 시간을 뺌
                if remain_time >= stop_playtime:
                    answer.append(stop_subject)
                    remain_time -= stop_playtime
                # 과제를 마치는 데 걸리는 시간이 남은 시간보다 크면 과제를 다 마치지 못한 것
                # 다시 멈춰둔 과제 배열에 저장하는데 남은 시간에서 잔여 시간을 뺌
                # 잔여 시간은 0으로 변경
                else:
                    subject.append([stop_subject, stop_start, stop_playtime - remain_time])
                    remain_time = 0
        # 현재 과제가 끝나는 예정 시간이 다음 과제의 시작 시간보다 크면 멈춰둔 과제 배열에 저장
        # 잔여 시간은 과제를 마치는 데 걸리는 시간에서 현재 과제의 시작 시간과 다음 과제의 시작 시간 사이의 값을 뺌
        else:
            plans[i][2] = playtime - (n_start - start)
            subject.append(plans[i])
    # print(answer)
    # print(subject)
    # 가장 최근에 멈춘 과제부터 시작하니까 뒤에서부터 가져옴
    for s in subject[::-1]:
        answer.append(s[0])
        
    return answer