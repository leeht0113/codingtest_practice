from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    discount = [0.1, 0.2, 0.3, 0.4]
    d_list = list(product(discount, repeat=len(emoticons)))
    max_service = 0 # 최대 이모티콘 서비스 가입자 
    max_sales = 0 # 최대 판매액
    for d in d_list: # 각 이모티콘의 할인율
        service = 0 # 서비스 가입자
        total = 0 # 총 구매비용
        for user in users:
            purchase = 0
            for idx, i in enumerate(d):
                if i >= (user[0]/100): # 일정 비율 이상 할인하는 이모티콘을 구매
                    purchase += (emoticons[idx] * (1 - i))
            if purchase >= user[1]: # 구매 비용의 합이 일정 가격 이상이 된다면,
                # 이모티콘 구매를 모두 취소하고, 이모티콘 플러스 서비스에 가입
                service += 1
            else: # 구매 비용의 합이 일정 가격 이하이면, 총 구매비용에 더함
                total += purchase
        if service >= answer[0]:
            if service == answer[0]:
                answer[1] = max(answer[1], total)
                # print(service, total, d, answer)
                continue
            else:
                # print(1)
                answer[1] = total
            answer[0] = service
            # print(answer, 2)
    return answer