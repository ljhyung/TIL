# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())              # 그리디하게 풀어서 반례가 많이 생긴다
# for tc in range(1, T+1):
#     N = int(input())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#     nlst = [[[]]*N for _ in range(N)]
#     visited = [0,0] * N
#     res = 0
#     for i in range(N):
#         nlst[0][i] = [lst[0][i],1<<i]
#     for r in range(1,N):
#         for c in range(N):
#             maxcc = 0
#             cc=0
#             for i in range(N):
#                 for j in range(len(nlst[r-1][i])):
#                     if (1<<c)&nlst[r-1][i][j][1]==0:
#                         maxcc = nlst[r-1][i][j][0]
#                         cc = i
#                     nlst[r][c][i].append([lst[r-1][cc][j][0]*lst[r][c] , (1<<c) + lst[r-1][cc][j][1]])
#     result = 0
#     for i in range(N):
#         if result<lst[N-1][i][0]:
#             result = lst[N-1][i][0]
#     print(f'#{tc} {result*100/(100**N):6f}')