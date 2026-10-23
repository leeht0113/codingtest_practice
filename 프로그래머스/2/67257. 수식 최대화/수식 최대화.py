from itertools import permutations
import re

def toPostFix(tokens, priority):
    stack = [] # 연산자 스택
    postfix = [] # 출력 배열 (문자열)
    
    for token in tokens:            # 분리된 모든 식을 돌아보면서                
        if token.isdigit():         # 숫자면 곧바로 추가
            postfix.append(token)   
        else:
            if not stack:           # stack이 비어있으면 연산자 스택에 추가
                stack.append(token)
            else:
                while stack:        # 안 비어 있다면
                    if priority[token] <= priority[stack[-1]]: # 현재 연산자가 우선순위가 
                        postfix.append(stack.pop()) # 같거나 낮으면 
                        # 낮아지지 않을 때까지 기존 스택 비우기
                    else: 
                        break
                stack.append(token) # 현재 연산자가 우선순위가 더 높아지면 스택에 자기자신 추가
                
    while stack:                    # 모든 식을 다 돌았는데 연산자가 남으면
        postfix.append(stack.pop()) # 남는 연산자 털어 넣기
    
    return postfix

def calc(tokens):
    stack = [] # 숫자 스택
    
    for token in tokens: # 순회
        if token.isdigit(): # 숫자라면
            stack.append(int(token)) # 숫자 스택에 추가
            continue
            
        # 연산자를 만날 경우 스택 두 번 pop
        num1 = stack.pop()
        num2 = stack.pop()
        # 연산자 따라 처리 후 다시 숫자 스택에 삽입
        if token == '*':
            stack.append(num2 * num1)
        elif token == '+':
            stack.append(num2 + num1)
        else: # '-'
            stack.append(num2 - num1)
    
    return stack.pop()

def solution(expression):
    tokens = re.split(r'([-+*])', expression) # 모든 숫자와 연사자를 분리
    operators = ['+', '-', '*']
    answer = 0
    
    for i in list(permutations(operators)):
        priority = {o: p for p, o in enumerate(list(i))}
        # 임의로 지정한 연산자는 여기에서 사용
        postfix = toPostFix(tokens, priority)
        answer = max(answer, abs(calc(postfix)))
    
    return answer