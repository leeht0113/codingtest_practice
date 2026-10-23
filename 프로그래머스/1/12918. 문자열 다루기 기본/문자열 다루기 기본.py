import re

def solution(s):
    p = re.compile('^\d*$')
    if (len(s) == 4 or len(s) == 6) and p.match(s):
        return True
    else:
        return False