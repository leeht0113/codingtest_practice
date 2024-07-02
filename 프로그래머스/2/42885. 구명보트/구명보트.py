def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    start = 0
    last = len(people) - 1
    while start <= last:
        if people[start] + people[last] <= limit:
            last -= 1
        start += 1
        answer += 1
    return answer