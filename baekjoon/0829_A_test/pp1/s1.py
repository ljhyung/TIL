import sys
from collections import deque
from pprint import pprint

sys.stdin = open("sample_input.txt", "r")


def mark(r,c,d,i):
    lst[r][c]=-i
    queue = deque()
    queue.append([r,c,d])
    while queue:
        rr,cc,dd = queue.popleft()
        if dd==0:
            continue
        for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            if 0<=rr+dr<30 and 0<=cc+dc<30 and lst[rr+dr][cc+dc]>=0:
                lst[rr + dr][cc + dc] ^= 2**i
                queue.append([rr+dr, cc+dc, dd-1])


def bfs(r,c):
    global h1,h2, hr1,hc1,hr2,hc2
    queue = deque()
    queue.append([r, c])
    visited[r][c]=1
    while queue:
        rr, cc = queue.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0 <= rr + dr < 30 and 0 <= cc + dc < 30 and visited[rr + dr][cc + dc] == 0 and lst[rr+dr][cc+dc]!=0:
                visited[rr + dr][cc + dc] = 1
                queue.append([rr + dr, cc + dc])
                checknum = check(rr + dr, cc + dc)
                if flag==0:
                    if h1 <checknum:
                        h1 = checknum
                        hr1 = rr+dr
                        hc1 = cc+dc
                else:
                    if h2 <checknum:
                        h2 = checknum
                        hr2 = rr+dr
                        hc2 = cc+dc


def check(r,c):
    res = 0
    for i in range(1,N+1):
        if lst[r][c] & 2**i:
            res += 1
    return res


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    finalanswer = 0
    # 0,0이 15,15
    lst = [[0 for _ in range(30)] for _ in range(30)]
    visited = [[0 for _ in range(30)] for _ in range(30)]
    for i in range(1,N+1):
        r,c,d = map(int, input().split())
        mark(c+15,r+15,d,i)
    cnt = 0
    h1, h2 = 0,0
    hr1, hc1 = 0,0
    hr2, hc2 = 0,0
    flag = 0
    flag2 = 0
    for r in range(30):
        if flag2:
            break
        for c in range(30):
            if flag2:
                break
            if lst[r][c]>0 and visited[r][c]==0:
                cnt += 1
                if cnt>2:
                    # print(f'#{tc} -1')
                    flag2=1
                    continue
                bfs(r,c)
                flag += 1
    if flag2:
        print(f'#{tc} -1')
        continue
    for r in range(30):
        for c in range(30):
            if lst[r][c]<0:
                if cnt == 2:
                    finalanswer += min((abs(hr1-r)+abs(hc1-c)),(abs(hr2-r)+abs(hc2-c)))
                else:
                    finalanswer += abs(hr1 - r) + abs(hc1 - c)

    print(f'#{tc} {finalanswer}')
