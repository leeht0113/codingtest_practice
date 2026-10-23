def solution(n, arr1, arr2):
    answer = []
    arr1_binary = []
    arr2_binary = []
    for a in arr1:
        arr1_binary.append(bin(a)[2:].zfill(n))
    for a in arr2:
        arr2_binary.append(bin(a)[2:].zfill(n))
    for a, b in zip(arr1_binary, arr2_binary):
        temp = ''
        for i, j in zip(a, b):
            if i == '1' or j == '1':
                temp += '#'
            elif i == '0' and j == '0':
                temp += ' '
        answer.append(temp)  
    return answer