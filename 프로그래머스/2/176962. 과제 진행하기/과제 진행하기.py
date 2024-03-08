def solution(plans):
    answer = []
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        total = h * 60 + m
        plans[i][1] = total
        plans[i][2] = int(plans[i][2])
    plans.sort(key = lambda x: x[1])
    subject = []
    for i in range(len(plans)):
        if i == len(plans) - 1:
            subject.append(plans[i])
            break
        cur_subject, start, playtime = plans[i]
        n_subject, n_start, n_playtime = plans[i + 1]
        if start + playtime <= n_start:
            answer.append(cur_subject)
            remain_time = n_start - (start + playtime)
            while remain_time != 0 and subject:
                stop_subject, stop_start, stop_playtime = subject.pop()
                if remain_time >= stop_playtime:
                    answer.append(stop_subject)
                    remain_time -= stop_playtime
                else:
                    subject.append([stop_subject, stop_start, stop_playtime - remain_time])
                    remain_time = 0
        else:
            plans[i][2] = playtime - (n_start - start)
            subject.append(plans[i])
    
    for s in subject[::-1]:
        answer.append(s[0])
        
    return answer