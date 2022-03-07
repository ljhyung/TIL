
dr = [-1,-1,-1,0,0,1,1,1]
dc = [-1,0,1,-1,1,-1,0,1]
N = 19
lst = [list(map(int, input().split())) for _ in range(N)]
valid = [[0]*N for _ in range(N)]
def omoc(lst):
    cnta = 0
    cntb = 0
    result = 0
    res = []
    for r in range(N):
        for c in range(N):
            for delta in range(8):
                rr = r
                cc = c
                if lst[rr][cc] == 1:
                    cnt1 = 0
                    while lst[rr][cc] == 1 and not valid[rr][cc] & (1<<delta):
                        valid[rr][cc] = valid[rr][cc] | (1<<delta)
                        cnt1 += 1
                        nr = rr + dr[delta]
                        nc = cc + dc[delta]
                        if 0 <= nr < N and 0 <= nc < N:
                            rr = nr
                            cc = nc
                        else:
                            boundary = False
                            break
                    else:
                        boundary = True
                    if cnt1 == 5:
                        cnta += 1
                        result = 1
                        res.append(r+1)
                        res.append(c+1)
                        if boundary:
                            res.append(rr - dr[delta]+1)        # nr이 범위 안 넘을 때는 빼면 안 됨
                            res.append(cc - dc[delta]+1)
                        else:
                            res.append(rr + 1)  # nr이 범위 안 넘을 때는 빼면 안 됨
                            res.append(cc + 1)
                #########
                elif lst[rr][cc] == 2:
                    cnt2 = 0
                    while lst[rr][cc] == 2 and not valid[rr][cc] & (1 << delta):
                        valid[rr][cc] = valid[rr][cc] | (1 << delta)
                        cnt2 += 1
                        nr = rr + dr[delta]
                        nc = cc + dc[delta]
                        if 0 <= nr < N and 0 <= nc < N:
                            rr = nr
                            cc = nc
                        else:
                            break
                    if cnt2 == 5:
                        cntb += 1
                        result = 2
                        res.append(r + 1)
                        res.append(c + 1)
                        res.append(rr - dr[delta]+1)
                        res.append(cc - dc[delta]+1)

    if cnta or cntb:
        if len(res)>2:
            if res[1] <= res[3]:
                print(result)
                print(res[0], res[1])
            else:
                print(result)
                print(res[2], res[3])
        else:
            print(result)
            print(res[0], res[1])
    else:
        print(0)
omoc(lst)

