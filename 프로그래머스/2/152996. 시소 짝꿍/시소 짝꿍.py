from collections import Counter

def solution(weights):
    result = 0
    counter = Counter(weights)
    for w, c in counter.items():
        if c >= 2:
            result += (c * (c - 1)) // 2
    weights = set(weights)
    for w in weights:
        if w * 2 in weights:
            result += counter[w*2] * counter[w]
        if w * (3/2) in weights:
            result += counter[w*(3/2)] * counter[w]
        if w * (4/3) in weights:
            result += counter[w*(4/3)] * counter[w]
    return result