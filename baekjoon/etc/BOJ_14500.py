'''
BOJ
테트로미노
골드 5
1시간
https://www.acmicpc.net/problem/14500
'''


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
maxsum = 0
dr = [0,1,0,-1]
dc = [1,0,-1,0]
# 1 ....
# for r in range(N):
#     for c in range(0,M-3):
#         s = sum(lst[r][c:c+4])
#         maxsum = max(maxsum, s)

# 2 .... 세로
# for c in range(M):
#     for r in range(0,N-3):
#         s = lst[r][c] + lst[r+1][c] + lst[r+2][c] + lst[r+3][c]
#         maxsum = max(maxsum, s)

# 3 네모
# for r in range(N-1):
#     for c in range(M-1):
#         s = sum(lst[r][c:c+2]) + sum(lst[r+1][c:c+2])
#         maxsum = max(maxsum, s)

# L 1
# for r in range(N-2):
#     for c in range(M-1):
#         s = lst[r][c] + lst[r+1][c] + lst[r+2][c] + lst[r+2][c+1]
#         maxsum = max(maxsum, s)

# ㅡㅡㅢ 2
# for r in range(N-1):
#     for c in range(M-2):
#         s = lst[r+1][c] + lst[r+1][c+1] + lst[r+1][c+2] + lst[r][c+2]
#         maxsum = max(maxsum, s)

# ㄱ 3
# for r in range(N-2):
#     for c in range(M-1):
#         s = lst[r][c] + lst[r][c+1] + lst[r+1][c+1] + lst[r+2][c+1]
#         maxsum = max(maxsum, s)

# rㅡㅡ 4
# for r in range(N-1):
#     for c in range(M-2):
#         s = lst[r][c] + lst[r][c+1] + lst[r][c+2] + lst[r+1][c]
#         maxsum = max(maxsum, s)

def dfs(r,c,prev,s,depth):
    global maxsum
    if depth==3:
        maxsum = max(maxsum, s+lst[r][c])
        return

    for i in range(4):
        if i==(prev+2)%4 and prev!=-1:
            continue
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<M:
            dfs(nr,nc,i,s+lst[r][c],depth+1)

maxsum = 0
for r in range(N):
    for c in range(M):
        dfs(r,c,-1,0,0)
        cnt = 0
        res = lst[r][c]

        if 0<=r-1:
            cnt += 1
            res += lst[r-1][c]

        if N > r + 1:
            cnt += 1
            res += lst[r+1][c]

        if c-1 >= 0:
            cnt += 1
            res += lst[r][c-1]

        if M > c + 1:
            cnt += 1
            res += lst[r][c+1]

        if cnt==3:
            maxsum = max(maxsum, res)
        elif cnt==4:
            tode = [lst[r-1][c],lst[r+1][c],lst[r][c-1],lst[r][c+1]]
            tode = min(tode)
            maxsum = max(maxsum, res-tode)

print(maxsum)

