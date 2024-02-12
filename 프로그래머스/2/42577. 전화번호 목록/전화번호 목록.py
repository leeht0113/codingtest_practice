def solution(phone_book):
    answer = True
    phone_dict = {}
    for p in phone_book:
        phone_dict[p] = 1
    for number in phone_book:
        temp = ''
        for n in number:
            temp += n
            if temp in phone_dict and temp != number:
                return False
    return answer