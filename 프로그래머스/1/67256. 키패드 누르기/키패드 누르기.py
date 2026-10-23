def dist(target, pos):
    return abs(target[0] - pos[0]) + abs(target[1] - pos[1])

def solution(numbers, hand):
    answer = []
    pos = {'L': [0, 3], 'R': [2, 3]}
    
    for n in numbers:
        if n in [1, 4, 7]:
            answer.append("L")
            pos["L"] = [0, (n - 1) // 3]
        elif n in [3, 6, 9]:
            answer.append("R")
            pos["R"] = [2, (n - 1) // 3]
        else:
            target = [1, 3 if n == 0 else (n - 1) // 3]
            left = dist(target, pos['L'])
            right = dist(target, pos['R'])
            
            if right < left:
                answer.append('R')
                pos['R'] = target
            elif right > left:
                answer.append('L')
                pos['L'] = target
            elif right == left:
                if hand == 'right':
                    answer.append('R')
                    pos['R'] = target
                elif hand == 'left':
                    answer.append('L')
                    pos['L'] = target
                
    return ''.join(answer)