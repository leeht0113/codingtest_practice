def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for i in my_string:
        if i not in vowels:
            answer += i
    return answer