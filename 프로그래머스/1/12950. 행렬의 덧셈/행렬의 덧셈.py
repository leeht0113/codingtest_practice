def solution(arr1, arr2):
    answer = []
    for x in range(len(arr1)):
        sublist = []
        for y in range(len(arr1[x])):
            sublist.append(arr1[x][y] + arr2[x][y])
        answer.append(sublist)
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]], [[3],[4]]))