def solution(id_pw, db):
    answer = 'fail'
    for id_, pw in db:
        if id_pw[0] == id_:
            if id_pw[1] == pw:
                answer = 'login'
            else:
                answer = 'wrong pw'
    return answer
                
                    