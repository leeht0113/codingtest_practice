def solution(s):
    stack = []
    for x in s:
        if x == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] == '(':
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False