import copy
from collections import deque


def dfs(now, visited, sheep, wolf, check):
    global maxsheep
    if visited[now]==1:
        return
    visited[now]=1
    if info[now]==1:
        wolf += 1
    else:
        sheep += 1
        maxsheep = max(maxsheep, sheep)

    if sheep <= wolf:
        return

    for i in lst[now]:
        if i:
            check.append(i)

    for next in check:
        nextcheck = [loc for loc in check if loc != next and not visited[loc]]
        dfs(next, copy.deepcopy(visited), sheep, wolf, nextcheck)




info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
# for i in range(len(info)):
#     if info[i]==0:
#         info[i]=-1
visited = [0]*len(info)
maxsheep = 0
lst = [[0,0] for _ in range(len(info))]
for i in range(len(edges)):
    if lst[edges[i][0]][0]==0:
        lst[edges[i][0]][0] = edges[i][1]
    else:
        lst[edges[i][0]][1] = edges[i][1]


dfs(0, visited, 0, 0, [])
print(maxsheep)
print(lst)