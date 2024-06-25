from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_hash = defaultdict(set)
    stoped = defaultdict(int)
    for r in report:
        a, b = r.split()
        if b not in report_hash[a]:
            stoped[b] += 1
        report_hash[a].add(b)
    for i in id_list:
        mail = 0
        for j in report_hash[i]:
            if stoped[j] >= k:
                mail += 1
        answer.append(mail)
    return answer