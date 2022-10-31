'''
https://school.programmers.co.kr/learn/courses/30/lessons/92343
양과 늑대
카카오 기출 레벨3
30분
'''

# import copy
#
# def dfs(now, visited, sheep, wolf, check):
#     global maxsheep
#     if visited[now]==1:
#         return
#     visited[now]=1
#     if info1[now]==1:
#         wolf += 1
#     else:
#         sheep += 1
#         maxsheep = max(maxsheep, sheep)
#
#     if sheep <= wolf:
#         return
#
#     for i in lst[now]:
#         if i:
#             check.append(i)
#
#     for next in check:
#         nextcheck = [loc for loc in check if loc != next and not visited[loc]]
#         dfs(next, copy.deepcopy(visited), sheep, wolf, nextcheck)
#
# def solution(info, edges):
#     global info1, lst
#     info1 = info
#     visited = [0]*len(info)
#
#     lst = [[0,0] for _ in range(len(info))]
#     for i in range(len(edges)):
#         if lst[edges[i][0]][0]==0:
#             lst[edges[i][0]][0] = edges[i][1]
#         else:
#             lst[edges[i][0]][1] = edges[i][1]
#
#
#     dfs(0, visited, 0, 0, [])
#     answer = maxsheep
#     return answer
#
# info1 = []
# lst = []
# maxsheep = 0

answer=0
def solution(info, edges):
    global answer
    for i in range(len(info)):
        if info[i]==0:
            info[i]=1
        else:
            info[i]=-1
    answer = 0
    edgeInfo = [[] for _ in range(len(info))]
    pathList = [0]
    for parent, child in edges:
        edgeInfo[parent].append(child)

    def dfs(sheep, wolf, pathList):
        global answer
        if len(pathList)==0:
            answer = max(answer, sheep)
            return

        for i in range(len(pathList)):
            next = pathList[i]
            if sheep - wolf + info[next] > 0:
                if info[next] > 0:
                    newPathList = pathList[:]
                    newPathList.pop(i)
                    newPathList += edgeInfo[next]
                    dfs(sheep + 1, wolf, newPathList)
                else:
                    newPathList = pathList[:]
                    newPathList.pop(i)
                    newPathList += edgeInfo[next]
                    dfs(sheep, wolf + 1, newPathList)
            else:
                answer = max(answer, sheep)

    dfs(0, 0, pathList)
    return answer




print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))