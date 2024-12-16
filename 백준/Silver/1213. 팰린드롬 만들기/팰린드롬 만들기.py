from collections import Counter

s = Counter(input())
if sum(i % 2 for i in s.values()) > 1:
    print("I'm Sorry Hansoo")
else:
    half = ''
    for k, v in sorted(s.items()):
        half += k * (v // 2)
    answer = half
    for k, v in s.items():
        if v % 2:
            answer += k
    answer += ''.join(half[::-1])
    print(answer)