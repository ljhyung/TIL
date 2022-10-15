'''
codetree
꼬리잡기놀이
기출
2시간 미해결
'''




from collections import deque
from pprint import pprint

n,m,k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
res = 0
teamcheck = [[-1 for _ in range(n)] for _ in range(n)]

teams = []
def bfs(r,c):
    teams.append([[r,c]])
    queue = deque()
    queue.append([r,c])
    while queue:
        r,c = queue.popleft()
        teamcheck[r][c] = len(teams)-1
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
            if teamcheck[nr][nc]>=0:continue
            if lst[nr][nc] == 2:
                teams[-1].append([nr,nc])
                queue.append([nr,nc])
                break
            elif lst[nr][nc]==3:
                teams[-1].append([nr, nc])
                return

def bfs2(r,c):
    queue = deque()
    queue.append([r, c])
    while queue:
        r,c = queue.popleft()
        teamcheck[r][c] = len(teams)-1
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
            if teamcheck[nr][nc]>=0:continue
            if lst[nr][nc] != 0:
                queue.append([nr,nc])




def run():
    for team in teams:
        r = team[0][0]
        c = team[0][1]
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
            if lst[nr][nc] == 4:
                lst[nr][nc] = 1
                lst[r][c] = 2
                lst[team[-1][0]][team[-1][1]]=4
                lst[team[-2][0]][team[-2][1]] = 3
                for i in range(len(team)-1):
                    team[-1-i] = team[-1-i-1]
                team[0] = [nr,nc]



def roundd(k):
    global res
    k%=4*n
    dir = (k-1)//n
    di = (k-1)%n
    if dir==0:
        sr = k-1
        sc = 0
        dr,dc=0,1
    elif dir==1:
        sr = n-1
        sc = di
        dr, dc = -1, 0
    elif dir==2:
        sr = n-1-di
        sc = n-1
        dr, dc = 0, -1
    else:
        sr = 0
        sc = n-1-di
        dr, dc = 1, 0


    while True:
        if sr<0 or sr>=n or sc<0 or sc>=n:break
        if lst[sr][sc]!=4 and lst[sr][sc]!=0:
            t = teamcheck[sr][sc]
            # for t in range(len(teams)):
                # if [sr,sc] in teams[t]:
            for i in range(len(teams[t])):
                if teams[t][i] == [sr,sc]:
                    res += (i+1)**2
                    lst[teams[t][0][0]][teams[t][0][1]] = 3
                    lst[teams[t][-1][0]][teams[t][-1][1]] = 1
                    teams[t] = teams[t][::-1]
                    return

        else:
            sr += dr
            sc += dc





for r in range(n):
    for c in range(n):
        if lst[r][c]==1:
            bfs(r,c)
            bfs2(r,c)
# print(teams)
# pprint(teamcheck)
cntt = 1
while k:
    run()
    roundd(cntt)
    cntt+=1
    k-=1

print(res)

# pprint(teamcheck)

# pprint(lst)
#
# lst = [1,2,3]
# print(lst[-1:-4:-1])