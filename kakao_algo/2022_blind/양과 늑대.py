from collections import deque


def dfs(n, cnt, sheep):
    global maxsheep
    if info[n]==-1:
        cnt -= 1
        sheep += 1
    else:
        cnt += 1
    if cnt>=0:
        return
    if maxsheep<sheep:
        maxsheep=sheep
    for i in lst[n]:
        if i:
            dfs(i, cnt, sheep)



info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
for i in range(len(info)):
    if info[i]==0:
        info[i]=-1

lst = [[0,0] for _ in range(len(info))]
for i in range(len(edges)):
    if lst[edges[i][0]][0]==0:
        lst[edges[i][0]][0] = edges[i][1]
    else:
        lst[edges[i][0]][1] = edges[i][1]


maxsheep = 0
dfs(0, 0, 0)
print(maxsheep)