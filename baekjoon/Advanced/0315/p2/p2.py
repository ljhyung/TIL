import sys
sys.stdin = open("input.txt", "r")


# def mindes(hunter, togos):
#     result = 2*N
#     for togo in togos:
#         des = abs(hunter[0]-togo[0]) + abs(hunter[1]-togo[1])
#         if result > des:
#             result = des
#             num = togo[2]
#     return [result, num]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    # monster_lst = []
    # monster_stack = []
    # house_lst = []
    # now = [0, 0]
    # cnt = 0
    # for i in range(N):
    #     for j in range(N):
    #         if lst[i][j]>0:
    #             monster_lst.append([i,j,lst[i][j]])
    #         elif lst[i][j]<0:
    #             house_lst.append([i,j,abs(lst[i][j])])
    # while monster_lst and house_lst:
    #     if monster_stack==0:
    #         temp = mindes(now, monster_lst)
    #         now = monster_lst[temp[1]][:1]
    #         cnt += temp[0]
    #         monster_stack.append(temp[1])
    #         monster_lst.pop(monster_lst.index(temp[1]))
    #
    # print(cnt)
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    r = 0
    c = 0
    goto = []
    house = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if lst[i][j]>0:
                goto.append(lst[i][j])

    for delta in range(8):
        nr = r + dr[delta]
        nc = c + dc[delta]
        if 0<=nr<N and 0<=nc<N and lst[nr][nc]!=0 and ((lst[nr][nc] in goto) or (lst[nr][nc] in house)):
            cnt += abs(r-nr)+abs(c-nc)
            r = nr
            c = nc
















