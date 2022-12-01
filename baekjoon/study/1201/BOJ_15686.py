'''
https://www.acmicpc.net/problem/15686
치킨 배달
골드5

'''
import copy
import heapq
N, M = map(int, input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
homeList = []
chickList = []
for r in range(N):
    for c in range(N):
        if lst[r][c]==1:
            homeList.append([r,c])
        elif lst[r][c]==2:
            chickList.append([r,c])
distList = [[] for _ in range(len(homeList))]
for i in range(len(homeList)):
    tempR, tempC = homeList[i]
    for idx,[cR,cC] in enumerate(chickList):
        heapq.heappush(distList[i],[abs(tempR-cR)+abs(tempC-cC),idx])
chickAll = len(chickList)
finalResult = float('inf')

def search(killList):
    answer = 0
    temp = copy.deepcopy(distList)
    for i in range(len(temp)):
        while temp[i]:
            distance, chickIdx = heapq.heappop(temp[i])
            if chickIdx in killList:
                continue
            else:
                answer+=distance
                break
    # print("answer : ",answer)
    return answer


def dfs(depth,killNum,killList):
    global finalResult
    if killNum==chickAll-M:
        finalResult = min(search(killList),finalResult)
        return
    if depth==chickAll:
        return
    if chickAll-depth<chickAll-M-killNum:
        return

    dfs(depth+1,killNum+1,killList+[depth])
    dfs(depth+1,killNum,killList)


dfs(0,0,[])
# print(distList)
#
# print(lst)
print(finalResult)