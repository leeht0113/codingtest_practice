def solution(n, results):
    # n x n 크기의 2차원 배열 생성
    total = [[0 for i in range(n)] for j in range(n)]
    # 대각선 자리는 자기 자신이므로 접근할 필요가 없다는 것을 표기
    for i in range(n):
        total[i][i] = 'SELF'
        
    # 주어진 결과에서 승/패 정보를 기록
    # 양방향에서 승/패를 기록
    for result in results:
        total[result[0] - 1][result[1] - 1] = 'WINS'
        total[result[1] - 1][result[0] - 1] = 'LOSE'
        
    # 플로이드-워셜 알고리즘을 사용해 가능한 빈 공간을 모두 채워 넣음
    # i번 선수가 k번 선수를 이겼고, k번 선수가 j번 선수를 이겼다면 i번 선수는
    # 반드시 j번 선수를 이김
    # 반대도 가능
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if total[i][k] == 'WINS' and total[k][j] == 'WINS':
                    total[i][j] = 'WINS'
                elif total[i][k] == 'LOSE' and total[k][j] == 'LOSE':
                    total[i][j] = 'LOSE'
                    
    # 각 선수가 누락된 정보 없이 승패를 모두 채웠다면, 모든 요소를 가득 채웠을 것임
    # 모두 채운 선수가 몇 명인지 구함
    answer = 0

    for i in total:
        # 각 행 리스트에 0이 없는지 확인
        if 0 not in i:
            answer += 1
    return answer