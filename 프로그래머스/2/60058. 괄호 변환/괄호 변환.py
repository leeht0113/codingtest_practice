def check(p):
    stack = []
    for x in p:
        if x == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            elif stack[0] == '(':
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
    
def balance(p):
    left_b = 0
    right_b = 0
    for idx, i in enumerate(p):
        if i == "(":
            left_b += 1
        elif i == ")":
            right_b += 1
        if left_b == right_b:
            u = p[:idx + 1]
            v = p[idx + 1:]
            return u, v

def reverse(u):
    temp = ''
    u = u[1:-1]
    for i in u:
        if i =="(":
            temp += ")"
        elif i == ")":
            temp += '('
    return temp
        
def solution(p):
    answer = ''
    if len(p) == 0:
        return ''
    if check(p):
        return p
    u, v = balance(p)
    # print(u, v)
    if check(u):
        return u + solution(v)
    else:
        temp = '(' + solution(v) + ')'
        temp += reverse(u)
        return temp