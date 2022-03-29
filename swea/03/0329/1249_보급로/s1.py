# import sys
# from collections import deque
# from pprint import pprint
#
# sys.stdin = open("input.txt", "r")
#
# dr = [0, 1, 0, -1]        # 시간 초과 맨이야~
# dc = [1, 0, -1, 0]
#
# def  sol():
#     global res
#     queue = deque()
#     queue.append((0,0))
#     sumlst[0][0]=0
#     while queue:
#         r, c = queue.popleft()
#         for delta in range(2):
#             nr = r + dr[delta]
#             nc = c + dc[delta]
#             if 0 <= nr < N and 0 <= nc < N:
#                 sumlst[nr][nc] = min(sumlst[nr][nc], sumlst[r][c] + lst[nr][nc])
#                 if sumlst[nr][nc]<=min(res, sumlst[N-1][N-1]):
#                     queue.append((nr,nc))
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = [list(map(int, input())) for _ in range(N)]
#     sumlst = [[9*N*N]*N for _ in range(N)]
#     res = sum(lst[0])+sum(list(zip(*lst))[N-1])
#     sol()
#     # pprint(sumlst)
#     print(f'#{tc} {sumlst[N-1][N-1]}')