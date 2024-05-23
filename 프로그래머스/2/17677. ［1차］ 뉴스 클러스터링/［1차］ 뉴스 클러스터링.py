def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    # print(str1, str2)
    dict_a = {}
    dict_b = {}
    for s in range(len(str1) - 1):
        temp = str1[s] + str1[s+1]
        # print(temp)
        if temp.isalpha():
            dict_a[temp] = dict_a.get(temp, 0) + 1
    # print('-------------')
    for s in range(len(str2) - 1):
        temp = str2[s] + str2[s+1]
        # print(temp)
        if temp.isalpha():
            dict_b[temp] = dict_b.get(temp, 0) + 1
    # print(dict_a)
    # print(dict_b)
    set_a = set(dict_a.keys())
    set_b = set(dict_b.keys())
    # print(set_a)
    # print(set_b)
    # print(set_a & set_b)
    common = set_a & set_b
    # print(common)
    intersect = 0
    union = sum(dict_a.values()) + sum(dict_b.values())
    for c in common:
        intersect += min(dict_a[c], dict_b[c])
        # union += max(dict_a[c], dict_b[c])
    # print(intersect)
    union -= intersect
    # print(union)
    if intersect == 0 and union == 0:
        return 65536
    answer = (intersect / union)
    answer *= 65536
    return int(answer)