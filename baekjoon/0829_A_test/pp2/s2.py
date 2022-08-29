import sys
from pprint import pprint

sys.stdin = open("sample_input.txt", "r")


def sol(now, lst, dist, cnt, depth):
    global answer, finalcnt, finalist
    if cnt+core-depth<finalcnt:
        return
    nr,nc = now[0], now[1]
    for r in range(nr,N):
        for c in range(N):
            if r==nr and c<=nc:
                continue
            if lst[r][c]==1:
                if r == 0 or r == N - 1 or c == 0 or c == N - 1:
                    cnt += 1
                    depth+=1
                    continue
                if r==1 and lst[r-1][c]==0:
                    lst[r - 1][c] =2
                    cnt += 1
                    dist += 1
                    depth+=1
                    continue
                if r==N-2 and lst[r+1][c]==0:
                    lst[r + 1][c] =2
                    cnt += 1
                    dist += 1
                    depth+=1
                    continue
                if c==1 and lst[r][c-1]==0:
                    lst[r][c - 1] =2
                    cnt += 1
                    dist += 1
                    depth+=1
                    continue
                if c==N-2 and lst[r][c+1]==0:
                    lst[r][c + 1] =2
                    cnt += 1
                    dist += 1
                    depth+=1
                    continue
                #check
                for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                    nnr, nnc = r+dr,c+dc
                    nlst = list(map(lambda x: x[:], lst))
                    flag = 0
                    ccnt = 0
                    while 0<=nnr<N and 0<=nnc<N:
                        if nlst[nnr][nnc]==0:
                            nlst[nnr][nnc]=2
                            nnr += dr
                            nnc += dc
                            ccnt += 1
                        else:
                            flag=1
                            break
                    if flag==0:
                        sol([r,c], nlst, dist+ccnt, cnt+1, depth+1)
                # 전원 연결 안 했을 때
                sol([r,c], lst, dist, cnt, depth+1)
    if cnt>=finalcnt:
        answer = min(answer, dist)
        finalcnt = cnt
        finalist = lst


T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    answer = float('inf')
    finalcnt = 0
    finalist = []
    lst = [list(map(int, input().split())) for _ in range(N)]
    core = sum(map(sum, lst))
    sol([0,0], lst, 0, 0, 0)



    print(f'#{tc} {answer}')
    # pprint(finalist)