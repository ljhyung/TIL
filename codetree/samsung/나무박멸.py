n, m, k, C = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]

result = 0
for r in range(n):
    for c in range(n):
        if lst[r][c]==-1:
            lst[r][c]=-10001
def grow():
    for r in range(n):
        for c in range(n):
            if lst[r][c]<=0:continue
            cnt =0
            for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                nr = r+dr
                nc = c+dc
                if 0<=nr<n and 0<=nc<n and lst[nr][nc]>0:
                    cnt += 1
            lst[r][c]+=cnt

def spread():
    templst = [[0 for _ in range(n)] for _ in range(n)]             # 동시에 퍼지므로 표시할 배열 생성
    for r in range(n):
        for c in range(n):
            if lst[r][c]<=0:continue
            cnt =0
            for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < n and lst[nr][nc] == 0:    # 심을 수 있으면 cnt +=1
                    cnt += 1
            for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < n and lst[nr][nc] == 0:
                    templst[nr][nc]+=lst[r][c]//cnt     # 심기
    for r in range(n):
        for c in range(n):
            lst[r][c] += templst[r][c]      # 적용

def kill():
    global result
    tempr = n
    tempc = n
    tempkill = 0
    for r in range(n):
        for c in range(n):
            if lst[r][c]>0:
                cnt=lst[r][c]
                for dr,dc in [[-1,-1],[1,1],[1,-1],[-1,1]]:
                    for i in range(1,k+1):
                        nr = r+i*dr
                        nc = c+i*dc
                        if nr<0 or nr>=n or nc<0 or nc>=n:continue  # 범위 밖이면 넘기는데 break하는게 더 좋을듯
                        if lst[nr][nc]<=0:          # 나무가 아니면 그만
                            break
                        cnt += lst[nr][nc]
                if tempkill>cnt:continue            # 최대값 찾기
                elif tempkill == cnt:
                    if tempr>r:
                        tempr=r
                        tempc=c
                    elif tempr==r and tempc>c:
                        tempc=c
                else:
                    tempkill=cnt
                    tempr = r
                    tempc = c
    if tempr == n or tempc == n:return              # 런타임에러 나와서 넣었습니다
    if lst[tempr][tempc]<=0:return                  #
    result += tempkill
    # print(tempkill)
    # print(tempr, tempc)
    for dr, dc in [[-1, -1], [1, 1], [1, -1], [-1, 1]]: # 살충제 뿌리기
        for i in range(1, k + 1):
            nr = tempr + i * dr
            nc = tempc + i * dc
            if nr < 0 or nr >= n or nc < 0 or nc >= n: break
            # if lst[nr][nc] <= 0:
            #     break
            # else:
            if lst[nr][nc]==0:              # 빈 곳이면 뿌리고 그만
                lst[nr][nc] = -C - 1
                break
            if lst[nr][nc]<-8000: break     # 벽 설정을 잘 할 것
            if -8000<lst[nr][nc]<0:         # 이미 뿌려진 곳이면 새로 갱신하고 그만
                lst[nr][nc] = -C - 1
                break
            lst[nr][nc]=-C-1

    lst[tempr][tempc]=-C-1                  # 지정 자리 뿌리기
    for r in range(n):
        for c in range(n):
            if lst[r][c]<0:
                lst[r][c]+=1                # 1년 지나기


# def kill():
#     global result
#     rd = [0 for _ in range(2*n-1)]
#     ld = [0 for _ in range(2*n-1)]
#     for r in range(n):
#         for c in range(n):
#             if lst[r][c]>0:
#                 rd[r-c+n-1] += lst[r][c]
#                 ld[r+c] += lst[r][c]
#     tempr = n
#     tempc = n
#     tempkill = 0
#     for r in range(n):
#         for c in range(n):
#             if tempkill>rd[r-c+n-1]+ld[r+c]-lst[r][c]:continue
#             elif tempkill==rd[r-c+n-1]+ld[r+c]-lst[r][c]:
#                 if tempr>r:
#                     tempr=r
#                 elif tempr==r and tempc>c:
#                     tempc=c
#             else:
#                 tempkill=rd[r-c+n-1]+ld[r+c]-lst[r][c]
#                 tempr = r
#                 tempc = c
#     result += tempkill
#     for r in range(n):
#         for c in range(n):
#             if r-c==tempr-tempc:
#                 lst[r][c]=-c-1
#             if r+c==tempr+tempc:
#                 lst[r][c]=-c-1
#     for r in range(n):
#         for c in range(n):
#             if lst[r][c]<0:
#                 lst[r][c]+=1


while m:
    grow()
    spread()
    kill()
    m-=1

print(result)