from collections import deque


def solution(alp, cop, problems):
    global minCost, answer, proList, lst

    answer = 0
    alpMax = max(map(lambda x:x[0], problems))
    copMax = max(map(lambda x:x[1], problems))
    lst = [[float('inf') for _ in range(alpMax+1)] for _ in range(copMax+1)]
    # proList = []

    minCost = float('inf')

    def bfs():
        global minCost, answer, proList, lst
        queue = deque()
        # proList = checkPro(alp, cop, proList)
        queue.append([alp, cop, 0])

        while(queue):
            alpNow, copNow, costNow = queue.popleft()
            if alpNow>alpMax:alpNow=alpMax
            if copNow>copMax:copNow=copMax
            if lst[copNow][alpNow]>costNow: lst[copNow][alpNow]=costNow
            else:continue
            # if(costNow>=minCost):
            #     continue
            # if(alpNow>=alpMax and copNow>=copMax):
            #     minCost = min(minCost, costNow)
            if(alpNow<alpMax):
                queue.append([alpNow+1, copNow, costNow+1])
            if(copNow<copMax):
                queue.append([alpNow, copNow+1, costNow+1])
            for i in range(len(problems)):
                if problems[i][0]<=alpNow and problems[i][1]<=copNow:
                    queue.append([alpNow+problems[i][2], copNow+problems[i][3], costNow+problems[i][4]])


    def checkPro(alpNow, copNow, proListNow):
        # temp = []
        # kill = []
        for pro in problems:
            if ((pro not in proListNow) and pro[0]<=alpNow and pro[1]<=copNow):
                proListNow.append(pro)
        #         temp.append(pro)
        # if not temp: return proListNow
        # for k in range(len(temp)):
        #     for i in range(len(proListNow)):
        #         if (temp[k][4]<=proListNow[i][4] and temp[k][2]>=proListNow[i][2] and temp[k][3]>=proListNow[i][3]):
        #             kill.append(i)
        # if not kill:
        #     for k in range(len(temp)):
        #         proListNow.append(temp[k])
        #     return proListNow
        # for j in range(len(kill)):
        #     proListNow.pop(kill[len(kill)-1-j])
        # for k in range(len(temp)):
        #     proListNow.append(temp[k])
        return proListNow

    bfs()
    # answer = minCost
    answer = lst[copMax][alpMax]
    return answer

print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))