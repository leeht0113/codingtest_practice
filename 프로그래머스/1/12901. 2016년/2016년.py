import datetime

def solution(a, b):
    day = {0:'MON',1:'TUE',2:'WED',3:'THU',4:'FRI',5:'SAT',6:'SUN'}
    answer = datetime.date(2016,a,b).weekday()
    return day[answer]