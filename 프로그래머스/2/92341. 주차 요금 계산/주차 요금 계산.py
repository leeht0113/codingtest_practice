from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    f_time = fees[0]
    fee = fees[1]
    extra_time = fees[2]
    extra_fee = fees[3]
    intime_dict = {}
    in_dict = defaultdict(int)
    sum_dict = defaultdict(int)
    last_time = 23 * 60 + 59
    for r in records:
        time, number, detail = r.split()
        time = list(map(int, time.split(':')))
        time = time[0] * 60 + time[1]
        if detail == "IN":
            intime_dict[number] = time
            in_dict[number] = 1
        else:
            sum_dict[number] += (time - intime_dict[number])
            in_dict[number] = 0
    for i in in_dict:
        if in_dict[i] == 1:
            sum_dict[i] += (last_time - intime_dict[i])
    car = list(sorted(sum_dict.keys()))
    for c in car:
        cost = fee + max(math.ceil((sum_dict[c] - f_time)/extra_time), 0) * extra_fee
        answer.append(cost)
    return answer