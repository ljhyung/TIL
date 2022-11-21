'''
https://www.acmicpc.net/problem/14466
소가 길을 건너간 이유 6
골드4
1시간
'''

N,K,R = map(int, input().split())
bridge = dict()
lst = [[0 for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
group = []
for _ in range(R):
    r1,c1,r2,c2 = map(int, input().split())
    r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1
    if bridge.get((r1,c1))!=None:bridge[(r1,c1)] += [[r2,c2]]
    else:bridge[(r1,c1)]= [[r2,c2]]
    if bridge.get((r2,c2))!=None:bridge[(r2,c2)] += [[r1,c1]]
    else:bridge[(r2,c2)]= [[r1,c1]]

for _ in range(K):
    r,c = map(int, input().split())
    lst[r-1][c-1]=1

def outRange(r,c):
    global N
    if r<0 or r>=N or c<0 or c>=N:
        return True
    else:return False


def bfs(sR,sC):
    group.append(0)
    cnt=0
    queue = [(sR,sC)]
    while queue:
        r,c = queue.pop(0)
        if visited[r][c]: continue
        if lst[r][c]==1:cnt += 1
        visited[r][c]=1
        for dr,dc in [[0,1], [0,-1], [1,0], [-1,0]]:
            nr,nc = r+dr, c+dc
            if outRange(nr,nc):continue
            if bridge.get((r,c))!=None and [nr,nc] in bridge.get((r,c)):continue
            if visited[nr][nc]:continue
            queue.append((nr,nc))
    group[-1] = cnt

for r in range(N):
    for c in range(N):
        if visited[r][c]==0:
            bfs(r,c)
result = 0
lenG = len(group)
for i in range(lenG):
    for j in range(i,lenG):
        if i==j:continue
        result+=group[i]*group[j]


print(result)


