import sys
sys.stdin = open("input.txt", "r")


# def mintime(depth, lst, cnt):
#     global result
#     if depth == 3:
#         if result > cnt:
#             result = cnt
#         return
#     else:
#         for i in range(3):
#             if visited[i]==0:
#                 visited[i] = 1
#                 fisher = fish[i][1]
#                 delta = 0
#                 while fisher:
#                     # if fisher == 1:
#                     #     for j in range(2):
#                     #         if j%2:
#                     #             if 0 <= fish[i][0] - delta < N and lst[fish[i][0] - delta] == 0:
#                     #                 lst[fish[i][0] - delta] = 1
#                     #                 fisher -= 1
#                     #                 cnt += (1 + delta)
#                     #                 mintime(depth + 1, lst, cnt)
#                     #             elif 0 <= fish[i][0] + delta < N and lst[fish[i][0] + delta] == 0:
#                     #                 lst[fish[i][0] + delta] = 1
#                     #                 fisher -= 1
#                     #                 cnt += (1 + delta)
#                     #                 mintime(depth + 1, lst, cnt)
#                     #         else:
#                     #             if 0 <= fish[i][0] + delta < N and lst[fish[i][0] + delta] == 0:
#                     #                 lst[fish[i][0] + delta] = 1
#                     #                 fisher -= 1
#                     #                 cnt += (1 + delta)
#                     #                 mintime(depth + 1, lst, cnt)
#                     #             elif 0 <= fish[i][0] - delta < N and lst[fish[i][0] - delta] == 0:
#                     #                 lst[fish[i][0] - delta] = 1
#                     #                 fisher -= 1
#                     #                 cnt += (1 + delta)
#                     #                 mintime(depth + 1, lst, cnt)
#                     # else:
#                     if 0<=fish[i][0]+delta<N and lst[fish[i][0]+delta]==0:  # 윗 주석 삭제 시 하나 들여쓰기
#                         lst[fish[i][0] + delta] = 1
#                         fisher -= 1
#                         cnt += (1+delta)
#                     if 0<=fish[i][0]-delta<N and lst[fish[i][0]-delta]==0:
#                         lst[fish[i][0] - delta] = 1
#                         fisher -= 1
#                         cnt += (1+delta)
#                     delta += 1
#                 mintime(depth+1, lst, cnt)
#                 visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    fish = []   # fish[0][0] - 출입구1, fish[0][1] - 낚시꾼1
    visited = [0, 0, 0]
    fish.append(list(map(int, input().split())))
    fish.append(list(map(int, input().split())))
    fish.append(list(map(int, input().split())))
    fish[0][0] -= 1
    fish[1][0] -= 1
    fish[2][0] -= 1
    result = 100000
    orders = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    for order in orders:
        lst = [0] * N
        cnt = 0
        for ord in order:
            fisher = fish[ord-1][1]
            delta = 0
            while fisher:
                if fisher and 0 <= fish[ord-1][0] - delta < N and lst[fish[ord-1][0] - delta] == 0:
                    lst[fish[ord-1][0] - delta] = 1
                    fisher -= 1
                    cnt += (1 + delta)
                if fisher and 0 <= fish[ord-1][0] + delta < N and lst[fish[ord-1][0] + delta] == 0:  # 윗 주석 삭제 시 하나 들여쓰기
                    lst[fish[ord-1][0] + delta] = 1
                    fisher -= 1
                    cnt += (1 + delta)
                delta += 1
        if result > cnt:
            result = cnt

    for order in orders:
        lst = [0] * N
        cnt = 0
        for ord in order:
            fisher = fish[ord-1][1]
            delta = 0
            while fisher:
                if fisher and 0 <= fish[ord-1][0] + delta < N and lst[fish[ord-1][0] + delta] == 0:  # 윗 주석 삭제 시 하나 들여쓰기
                    lst[fish[ord-1][0] + delta] = 1
                    fisher -= 1
                    cnt += (1 + delta)
                if fisher and 0 <= fish[ord-1][0] - delta < N and lst[fish[ord-1][0] - delta] == 0:
                    lst[fish[ord-1][0] - delta] = 1
                    fisher -= 1
                    cnt += (1 + delta)
                delta += 1
        if result > cnt:
            result = cnt
    print(f'#{tc} {result}')