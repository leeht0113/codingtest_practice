n = int(input())
scores = []
for _ in range(n):
    name, korean, english, math = input().split()
    scores.append([name, int(korean), int(english), int(math)])
scores = sorted(scores, key = lambda x: (-x[1], x[2], -x[3], x[0]))
for s in scores:
    print(s[0])