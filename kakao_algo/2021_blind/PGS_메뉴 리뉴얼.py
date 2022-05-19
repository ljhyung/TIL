'''
PGS
메뉴 리뉴얼
lv 2
1시간 30분
https://programmers.co.kr/learn/courses/30/lessons/72411
'''
from itertools import combinations


def solution(orders, course):
    def se(k):
        setms = []
        for i in range(N):
            setms += list(combinations(orders[i],k))
        setms = [''.join(sorted(list(f))) for f in setms]   # 이중 list는 set하면 unhashable이 뜬다 메모
        setms = list(set(setms))
        maxsetmlst = [0 for _ in range(len(setms))]
        for idx, setm in enumerate(setms):
            cnt = 0
            for i in range(N):
                for sem in setm:
                    if sem not in orders[i]:
                        break
                else:
                    cnt += 1
            maxsetmlst[idx] = cnt

        maxcnt = 0
        if maxsetmlst:
            maxcnt = max(maxsetmlst)


        if maxcnt<2:
            return
        for i in range(len(setms)):
            if maxsetmlst[i]==maxcnt:
                answer.append(''.join(setms[i]))

    answer = []
    orders = [list(f) for f in orders]
    N = len(orders)
    for k in course:
        se(k)
    answer.sort()
    print(answer)

    return answer


# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
solution(["XYZ", "XWY", "WXA"], [2,3,4])

