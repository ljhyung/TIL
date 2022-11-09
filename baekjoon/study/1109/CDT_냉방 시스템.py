'''
https://www.codetree.ai/frequent-problems/cooling-system/description
냉방 시스템
어려움

'''
from collections import deque

n,m,k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
powerList = [[0 for _ in range(n)] for _ in range(n)]
plusList = [[0 for _ in range(n)] for _ in range(n)]
controllerList = []
officeList = []
# 0000, 8 -> 위, 4 -> 왼쪽, 2 -> 아래, 1 -> 오른쪽
wallList = [[0 for _ in range(n)] for _ in range(n)]
dr = [0,1,0,-1]     # 0->오, 1->아래, 2->왼쪽, 3->위
dc = [1,0,-1,0]

def inRange(r,c):
    if 0 > r or r >= n or 0 > c or c >= n:
        return True
    return False


for _ in range(m):
    r,c,d = map(int,input().split())
    r-=1
    c-=1
    if d==0:
        wallList[r][c]|=8
        if r==n-1:continue
        wallList[r-1][c]|=2
    else:
        wallList[r][c]|=4
        if c==0:continue
        wallList[r][c-1]|=1

for r in range(n):
    for c in range(n):
        if lst[r][c]==1:
            officeList.append([r,c])
        elif lst[r][c]>0:
            controllerList.append([r,c,(lst[r][c])%4])

# make plus list
def coldGo():
    global plusList
    for r,c,d in controllerList:
        nr,nc = r+dr[d], c+dc[d]
        if 0>nr or nr>=n or 0>nc or nc>=n:continue
        if wallList[r][c]&d:continue
        queue = deque()
        queue.append([nr,nc,5])
        while queue:
            rr,cc,power = queue.popleft()
            plusList[rr][cc]=power
            if power==0:continue
            for delta in [-1,0,1]:
                if d==0 or d==2:# 오,왼
                    nextR, nextC = rr+delta, cc+dc[d]
                    if inRange(nextR,nextC):continue
                    if plusList[nextR][nextC]:continue
                    if delta==0:
                        if wallList[rr][cc]&2**d:continue
                        queue.append([nextR,nextC,power-1])
                    elif delta==-1:
                        if wallList[rr][cc]&8 or wallList[nextR][nextC]&2**((d+2)%4):continue
                        queue.append([nextR,nextC,power-1])
                    elif delta==1:
                        if wallList[rr][cc]&2 or wallList[nextR][nextC]&2**((d+2)%4):continue
                        queue.append([nextR,nextC,power-1])
                else:
                    nextR, nextC = rr + dr[d], cc + delta
                    if inRange(nextR,nextC):continue
                    if plusList[nextR][nextC]:continue
                    if delta==0:
                        if wallList[rr][cc]&2**d:continue
                        queue.append([nextR,nextC,power-1])
                    elif delta==-1:
                        if wallList[rr][cc]&4 or wallList[nextR][nextC]&2**((d+2)%4):continue
                        queue.append([nextR,nextC,power-1])
                    elif delta==1:
                        if wallList[rr][cc]&1 or wallList[nextR][nextC]&2**((d+2)%4):continue
                        queue.append([nextR,nextC,power-1])
        for r in range(n):
            for c in range(n):
                powerList[r][c]+=plusList[r][c]
                plusList[r][c] = 0

def spread():
    global powerList
    for r in range(n):
        for c in range(n):
            for d in range(4):
                nr = r+dr[d]
                nc = c+dc[d]
                if inRange(nr,nc):continue
                if wallList[r][c]&2**d:continue
                if powerList[r][c]-4<powerList[nr][nc]:continue
                spreadPower = (powerList[r][c]-powerList[nr][nc])//4
                plusList[nr][nc]+=spreadPower
                plusList[r][c]-=spreadPower
    for r in range(n):
        for c in range(n):
            powerList[r][c]+=plusList[r][c]
            plusList[r][c]=0

def side():
    for r in range(n):
        for c in range(n):
            if r==0 or r==n-1 or c==0 or c==n-1:
                powerList[r][c]-=1
                if powerList[r][c]<0:
                    powerList[r][c]=0

def check():
    for r,c in officeList:
        if powerList[r][c]<k:
            return False
    return True

cnt=0
while True:
    coldGo()
    spread()
    side()
    cnt+=1
    if cnt>100:
        cnt = -1
        break
    if check():break

print(cnt)
# add to real list
# spread
# kill bound
