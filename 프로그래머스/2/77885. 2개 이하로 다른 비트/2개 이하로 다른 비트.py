def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            n = '0' + bin(n)[2:]
            n = f"{n[:n.rindex('0')]}10{n[n.rindex('0')+2:]}"
            answer.append(int(n,2))
    return answer