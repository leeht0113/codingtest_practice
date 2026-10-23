def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell - set(s):
            return 1
    return 2