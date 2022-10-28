'''
https://www.acmicpc.net/problem/21277
짠돌이 호석
골드3
5시간
'''
import copy

r1, c1 = map(int, input().split())
lst1 = [list(map(int, input())) for _ in range(r1)]

r2, c2 = map(int, input().split())
lst2 = [list(map(int, input())) for _ in range(r2)]
nrcMax = 50*50



def rotate(lst2):
    nr = len(lst2[0])
    nc = len(lst2)
    nlst = [[0 for _ in range(nc)] for _ in range(nr)]
    for i in range(nr):
        nlst[i] = [lst2[nc-1-k][i] for k in range(nc)]
    return nlst


def area(r,c):
    ru, rd = 0, 0
    ru = r if r < nr2 else nr2
    rd = r + nr2 if r + nr2 > nr1 + nr2 else nr1 + nr2
    cr, cl = 0, 0
    cl = c if c < nc2 else nc2
    cr = nc2 + nc1 if c + nc2 < nc2 + nc1 else c + nc2

    temparea = abs(ru - rd) * abs(cr - cl)

    return temparea

def checkk():
    global nrcMax

    for r in range(nr1-2+nr2):
        for c in range(nc1 - 2 + nc2):
            temparea = area(r,c)
            if temparea >= nrcMax:
                continue

            templst = copy.deepcopy(nlst)


            flagg=False
            for rr in range(nr2):
                for cc in range(nc2):
                    templst[r+rr][c+cc] += lst2[rr][cc]
                    if templst[r+rr][c+cc]>1:
                        flagg=True
                        break
                if flagg:
                    break
            if flagg:
                continue

            nrcMax = min(nrcMax, temparea)


nr1 = len(lst1)
nc1 = len(lst1[0])
nr2 = len(lst2)
nc2 = len(lst2[0])
nlst = [[0 for _ in range(2 * nc2 + nc1)] for _ in range(2 * nr2 + nr1)]
for r in range(nr2, nr1 + nr2):
    for c in range(nc2, nc1 + nc2):
        nlst[r][c] = lst1[r - nr2][c - nc2]


for jjjj in range(4):
    checkk()

    lst2 = rotate(lst2)
    nr2, nc2 = nc2, nr2
    nlst = [[0 for _ in range(2 * nc2 + nc1)] for _ in range(2 * nr2 + nr1)]
    for r in range(nr2, nr1 + nr2):
        for c in range(nc2, nc1 + nc2):
            nlst[r][c] = lst1[r - nr2][c - nc2]

print(nrcMax)
