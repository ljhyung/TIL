import sys
input = sys.stdin.readline

N, M  = map(int, input().split())
lst = [[0]*(N+1)]
for _ in range(N):
    lst.append([0]+list(map(int, input().split())))


for r in range(1,N+1):
    for c in range(1,N+1):
        lst[r][c] += lst[r][c-1] + lst[r-1][c] - lst[r-1][c-1]



for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    res = lst[x2][y2]-lst[x1-1][y2]-lst[x2][y1-1]+lst[x1-1][y1-1]
    print(res)