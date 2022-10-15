'''
codetree
예술성
기출
2시간
'''

# # 반시계방향 90도 회전
# new_x = (n-1) - old_y
# new_y = old_x
#
# # 시계방향 90도 회전
# new_x = old_y
# new_y = (n-1) - old_x


from pprint import pprint

n = int(input())
N = (n-1)//2
group = 1
templst = [list(map(int, input().split())) for _ in range(n)]
lst = [[[0,0] for _ in range(n)] for _ in range(n)]     # 그룹도 함께 표시하기 위해 배열 정의

for r in range(n):
    for c in range(n):
        lst[r][c] = [templst[r][c],0]


visited = [[0 for _ in range(n)] for _ in range(n)]             # 그룹 나누기용
inclose = [[0 for _ in range(n**2+1)] for _ in range(n**2+1)]   # 그룹끼리 겹치는 면 표기용 배열
result = 0

def bfs(r,c):
    queue = []
    queue = [*queue,[r,c]]
    inclose[0][group] = lst[r][c][0]        # inclose 배열의 첫번째 행에 각 그룹이 나타내는 숫자 기록
    while queue:
        r,c = queue.pop(0)
        if visited[r][c]:continue
        visited[r][c]=1
        lst[r][c][1] = group
        for dr,dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr = r+dr
            nc = c+dc
            if nr<0 or nr>=n or nc<0 or nc>=n:continue
            if lst[r][c][0]==lst[nr][nc][0]:
                queue = [*queue,[nr,nc]]

def inclosed():
    for r in range(n):
        for c in range(n):
            if inclose[lst[r][c][1]][lst[r][c][1]]==0:
                inclose[lst[r][c][1]][lst[r][c][1]]=lst[r][c][1]    # 그룹 체크용 자리 채우기
                invisited = [[0 for _ in range(n)] for _ in range(n)]   # 방문 체크용
                queue = []
                queue = [*queue, [r, c]]
                while queue:
                    rr, cc = queue.pop(0)
                    if invisited[rr][cc]: continue
                    invisited[rr][cc]=1
                    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        nr = rr + dr
                        nc = cc + dc
                        if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
                        # if invisited[nr][nc]:continue                 # 같은 곳이라도 다른 방향에서면 겹치는 면이니깐 제외
                        if lst[nr][nc][0]==lst[rr][cc][0]:              # 같은 그룹
                            queue = [*queue,[nr,nc]]
                        else:                                           # 아니면 겹치는 면 추가 및 방문 표시
                            inclose[lst[rr][cc][1]][lst[nr][nc][1]] += 1
                            invisited[nr][nc] = 1                       # 필요한 부분은 아닌듯

def score():
    global result
    for r in range(n):
        for c in range(n):
            inclose[lst[r][c][1]][0] += 1   # inclose 배열의 첫 열에 각 그룹의 갯수 기록
    for r in range(1,n**2+1):
        for c in range(r+1,n**2+1):
            if inclose[r][c]>0:
                result += (inclose[r][0]+inclose[c][0])*inclose[0][r]*inclose[0][c]*inclose[r][c]   # (칸수+칸수) * 숫자 * 숫자 * 닿는면

def moveCross():

    for i in range(N):
        temp = lst[i][N]
        lst[i][N] = lst[N][n-1-i]
        lst[N][i], temp = temp, lst[N][i]
        lst[n-1-i][N], temp = temp, lst[n-1-i][N]   # 순서대로 옮기기
        lst[N][n-1-i], temp = temp, lst[N][n-1-i]


def moveSquare(R,C):
    nlst = [[[0,0] for _ in range(N)] for _ in range(N)]    # 1/4크기의 배열 만들어서 거기서 돌린거 기록 후 덮어씌우기
    for r in range(N):
        for c in range(N):
            nlst[r][c] = lst[R+N - 1 - c][C+r]              # 반시계 90도 가져오기

    for r in range(N):
        for c in range(N):
            lst[R+r][C+c] = nlst[r][c]


# 그룹 체크
for r in range(n):
    for c in range(n):
        if visited[r][c]==0:
            bfs(r,c)
            group+=1
inclosed()  # 닿는 면 체크
score()     # 점수 측정 및 합산

pprint(lst)
pprint(inclose)
for _ in range(3):
    # 이동
    moveSquare(0,0)
    moveSquare(N+1,0)
    moveSquare(0,N+1)
    moveSquare(N+1,N+1)
    moveCross()
    # 그룹 새로 짜기
    group = 1
    visited = [[0 for _ in range(n)] for _ in range(n)]
    inclose = [[0 for _ in range(n ** 2+1)] for _ in range(n ** 2+1)]
    for r in range(n):
        for c in range(n):
            if visited[r][c] == 0:
                bfs(r, c)
                group += 1
    # 닿는 면 체크
    inclosed()
    # 점수 합산
    score()




print(result)





