import re

def solution(phone_number):
    number_1 = re.sub('^\d*$', '*'*len(phone_number[:-4]), phone_number[:-4])
    return number_1 + phone_number[-4:]