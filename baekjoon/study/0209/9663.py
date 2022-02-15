# 각 퀸마다 값의 차등을 줘서 실패 시 빠져나올 수 있게 한다

import copy
from pprint import pprint

N = int(input())
N_real = copy.deepcopy(N)
check = []
cnt = 0
for i in range(N):
    lst = []
    for j in range(N):
        lst.append(False)
    check.append(lst)
pprint(check)

def queen_check(N_real,i,j,check):
    tempi, tempj = i, j
    for k in range(N_real):
        check[i][k] = True
        check[k][j] = True
    while i>0 and j>0: # 왼쪽 위
        i -= 1
        j -= 1
        check[i][j] = True
    i, j = tempi, tempj
    while i<N_real-1 and j>0: # 왼쪽 아래
        i += 1
        j -= 1
        check[i][j] = True
    i, j = tempi, tempj
    while i>0 and j<N_real-1: # 오른쪽 위
        i -= 1
        j += 1
        check[i][j] = True
    i, j = tempi, tempj
    while i<N_real-1 and j<N_real-1: # 오른쪽 아래
        i += 1
        j += 1
        check[i][j] = True

def queen(N, cnt, check):
    if not N:
        return cnt
    for i in range(N):
        for j in range(N):
            if not check[i][j]:
                cnt += 1
                queen_check(N_real,i,j,check)

    return queen(N-1, cnt, check)


queen_check(N_real,2,3,check)
pprint(check)


def is_promising(row):
    for i in range(row):
        if  queen[row] ==  queen[i] or abs( queen[row] -  queen[i]) == abs(row - i):
            return False

    return True


def n_queens(x):
    global ans
    if x == n:
        ans += 1

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
             queen[x] = i
            if is_promising(x):
                n_queens(x + 1)


n_queens(0)
print(ans)