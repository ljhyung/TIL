import copy
import sys
sys.stdin = open("sample_input.txt", "r")

def check123(lst):      # 다 만들어진 필름에서 조건 통과하는지만 체크
    # visited = [0] * W
    for c in range(W):
        maxtemp = 0
        temp = 0
        temp1 = lst[0][c]
        for r in range(D):
            if lst[r][c] == temp1:
                temp += 1
            else:
                temp1 = lst[r][c]
                temp = 1
            maxtemp = max(maxtemp, temp)
        # visited[c] = maxtemp
        if maxtemp<K:
            return False
    # for i in range(W):
    #     if visited[i] < K:
    #         return False
    return True





def makelst(ww, changelst):     # 보호필름 새로 갈아끼워서 결과 내는 함수
    global flag
    if flag:
        return

    if len(changelst)==ww:
        llst = copy.deepcopy(lst)
        #llst 변화
        for changels in changelst:
            r, k = changels
            llst[r] = [k]*W
        #temp변화
        if check123(llst):
            flag = True
        return

    for i in range(D):
        if i not in changelst:
            for k in range(2):
                makelst(ww, changelst + [[i, k]])
                if flag:
                    break
        if flag:
            break


def check(ww):

    # D중에서 ww개 고르기, ww개 고른거 A,B 고르기

    makelst(ww, [])
    #
    if flag:
        return True
    return False

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(D)]
    ww=0
    flag = False
    # flag2 = False
    while True:
        if check(ww):
            break
        # if not check(K-ww-1):
        #     flag2=True
        #     break
        # else:
        #     flag=False
        ww += 1
    # if flag2:
    #     ww = K-ww
    print(f'#{tc} {ww}')
