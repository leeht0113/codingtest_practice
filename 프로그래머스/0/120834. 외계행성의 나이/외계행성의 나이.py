from string import ascii_lowercase

def solution(age):
    answer = ''
    new_age = list(ascii_lowercase)[:10]
    age = str(age)
    for i in age:
        answer += new_age[int(i)]
    return answer