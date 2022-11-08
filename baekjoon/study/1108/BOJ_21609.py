'''
https://www.acmicpc.net/problem/21609
상어 중학교
골드2
1시간30분
'''
from pprint import pprint

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
Empty = " "
answer = 0

def search(r,c):
    num = lst[r][c]
    queue = [[r,c]]
    cnt = 1
    killList = [[r,c,num]]
    visited[r][c] = 1
    rainbowCnt=0
    while queue:
        r,c = queue.pop(0)
        for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
            nr = r+dr
            nc = c+dc
            if 0>nr or nr>=N or 0>nc or nc>=N:continue
            if visited[nr][nc]:continue
            if lst[nr][nc]==0 or lst[nr][nc]==num:
                visited[nr][nc] = 1
                queue.append([nr,nc])
                killList.append([nr,nc,lst[nr][nc]])
                if lst[nr][nc]==0:
                    rainbowCnt+=1
                cnt += 1
    killList.sort(key=lambda x:(-x[2],x[0],x[1]))
    if len(killList)>1:
        point.append([cnt,rainbowCnt,killList])
    for r,c,t in killList:
        if t==0:
            visited[r][c]=0
    return point


def kill(templst):
    global answer
    killList = templst[2]
    for r,c,t in killList:
        lst[r][c]=Empty
    answer += templst[0]**2
    # print(templst[0])

def gravity():
    '''
    빈칸 아래로 내리기, -1이면 제자리
    :return:
    '''
    for r in range(N-2,-1,-1):
        for c in range(N):
            if lst[r][c]==-1 or lst[r][c]==Empty:
                continue
            tempR = r
            while True:
                if tempR==N-1:break
                if lst[tempR+1][c]==Empty:
                    lst[tempR+1][c],lst[tempR][c]=lst[tempR][c],Empty
                    tempR+=1
                else:break



def rotate():
    global lst
    '''
    반시계 방향 90도 회전
    :return:
    '''
    templst = [[]for _ in range(N)]
    for i in range(N):
        temp = []
        for r in range(N):
            temp.append(lst[r][N-1-i])
        templst[i] = temp
    lst = templst


while True:
    point = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c]:continue
            if lst[r][c]==0 or lst[r][c]==-1 or lst[r][c]==Empty:continue
            search(r,c)
    if len(point)==0:
        break

    point.sort(key=lambda x:(-x[0],-x[1],-x[2][0][0],-x[2][0][1]))
    kill(point[0])
    gravity()
    rotate()
    gravity()


print(answer)
# gravity()
# pprint(lst)





