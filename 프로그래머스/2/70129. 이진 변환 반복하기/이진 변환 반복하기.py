def to_binary(n):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n%2) + result
        n //= 2
    return result

def solution(s):
    count, zero = 0, 0
    while s != "1":
        count += 1
        one_count = s.count("1")
        zero += len(s) - one_count
        s = to_binary(one_count)
    return count, zero