'''
알고력 코딩력 1시간 각1증가 문제풀어서 증가 다 푸는 능력 얻는 시간
[alp_req, cop_req, alp_rwd, cop_rwd, cost]
'''
def solution(alp, cop, problems):
    maxalgo, maxcod = 0, 0
    for problem in problems:
        maxalgo = max(maxalgo, problem[0])
        maxcod = max(maxcod, problem[1])
    

    answer = 0
    return answer


print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))