def solution(clothes):
    answer = 1
    cloth_dict = {}
    for c in clothes:
        cloth_dict[c[1]] = cloth_dict.get(c[1], []) + [c[0]]
    print(cloth_dict)
    for c in cloth_dict:
        answer *= (len(cloth_dict[c])+1)
    return answer - 1