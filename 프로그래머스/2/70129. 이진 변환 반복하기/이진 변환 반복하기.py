def solution(s):
    count = 0
    zero_count = 0
    while s != "1":
        zero_count += s.count("0")
        s = s.count("1")
        s = bin(s)
        count += 1
        s = s[2:]
    return [count, zero_count]