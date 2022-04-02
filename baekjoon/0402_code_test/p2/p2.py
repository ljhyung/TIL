grid = ["??b", "abc", "cc?"]



def check(result):
    for i in range(len(result)):
        nlst[num[i][0]][num[i][1]] = result[i]
    visited = [[0]*C for _ in range(N)]
    checklst = []
    checkcount = {'a':0, 'b':0, 'c':0}
    bet = 1
    for r in range(N):
        for c in range(C):
            if visited[r][c]==0:
                visited[r][c] = bet
                bet += 1
            checkcount[nlst[r][c]] += 1
            cnt = 0
            for delta in range(4):
                nr = r + dr[delta]
                nc = c + dc[delta]
                if 0<=nr<N and 0<=nc<C:
                    if nlst[r][c]==nlst[nr][nc]:
                        cnt += 1
                        visited[nr][nc] = visited[r][c]
            if cnt == 0:
                    checklst.append(nlst[r][c])
    cclst = []
    for k in visited:
        for kk in k:
            if kk not in cclst:
                cclst.append(kk)
    if len(cclst)>3:
        return False
    for i in ['a', 'b', 'c']:
        if checklst.count(i)>1:
            return False    # 성립 안 됨
        if checklst.count(i)==1 and checkcount[i]!=1:
            return False
    print(visited)
    return True



def sol(m,nlst,result):
    global res
    if m==M:
        if check(result):
            res += 1
        return
    for k in ['a', 'b', 'c']:
        sol(m+1,nlst,result+[k])


dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]


nnlst = grid

nlst = []
for i in nnlst:
    temp = []
    for k in range(len(i)):
        temp.append(i[k])
    nlst.append(temp)
N = len(nlst)
C = len(nlst[0])
num = []
res = 0
for i in range(N):
    for j in range(C):
        if nlst[i][j] == '?':
            num.append((i,j))
M = len(num)
sol(0,nlst,[])
print(res)
