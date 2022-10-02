from collections import deque


def solution(maps):
    cnt = 1
    R = len(maps)
    C = len(maps[0])
    lst = [["" for _ in range(C)]  for _ in range(R)]
    for i in range(R):
        for j in range(C):
            lst[i][j] = maps[i][j]

    visited = [[0 for _ in range(C)] for _ in range(R)]

    def bfs(r,c):
        alpha = dict()
        queue = deque()
        queue.append([r,c])
        while queue:
            rr,cc = queue.popleft()
            # if visited[rr][cc]: continue

            for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                nr = rr + dr
                nc = cc + dc
                if 0<=nr<R and 0<=nc<C and lst[nr][nc]!='.' and visited[nr][nc]==0:
                    queue.append([nr,nc])
                    visited[nr][nc] = cnt
                    if not alpha.get(lst[nr][nc]):
                        alpha[lst[nr][nc]] = [[nr,nc]]
                    else:
                        alpha[lst[nr][nc]] += [[nr,nc]]

        maxlen = 0
        maxal = ''
        maxlst = []
        flag = True
        for i in alpha.keys():
            if maxlen<len(alpha[i]):
                maxlen = len(alpha[i])
                maxal = i
        maxlst.append(maxal)
        for i in alpha.keys():
            if maxlen==len(alpha[i]):
                maxlst.append(i)
                if maxal!=i and ord(maxal)<ord(i):
                    maxal = i
            else:
                flag = False
        if flag:
            return
        else:
            for r in range(R):
                for c in range(C):
                    if visited[r][c]==cnt and lst[r][c] not in maxlst:
                        lst[r][c]=maxal


    for r in range(R):
        for c in range(C):
            if visited[r][c]==0:
                bfs(r,c)
                cnt += 1
    check = dict()
    for r in range(R):
        for c in range(C):
            if lst[r][c] == '.': continue
            if not check.get(lst[r][c]):
                check[lst[r][c]] = 1
            else:
                check[lst[r][c]] += 1
    answer = 0
    for i in check.keys():
        answer = max(answer, check[i])
    # print(lst)
    return answer


print(solution(["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]))
# print(solution(["XY..", "YX..", "..YX", ".AXY"]))