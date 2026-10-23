a, b = map(int, input().strip().split(' '))
answer = []
for i in range(b):
    temp = ''
    for j in range(a):
        temp += '*'
    answer.append(temp)
for a in answer:
    print(a)