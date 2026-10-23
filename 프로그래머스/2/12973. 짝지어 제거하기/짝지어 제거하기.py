def solution(s):
    stack = []
    for case in s:
        if stack and stack[-1] == case:
            stack.pop()
        else:
            stack.append(case)
    return 1 if len(stack) == 0 else 0