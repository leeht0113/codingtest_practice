def solution(participant, completion):
    participant_dict = {}
    for p in participant:
        participant_dict[p] = participant_dict.get(p, 0) + 1
    for c in completion:
        participant_dict[c] -= 1
        if participant_dict.get(c) == 0:
            del participant_dict[c]
    return list(participant_dict)[0]