def solution(people, limit):
    answer = 0
    people.sort()
    first = 0
    last = len(people) - 1
    while first <= last:
        if people[first] + people[last] <= limit:
            first += 1
        last -= 1
        answer += 1
    return answer