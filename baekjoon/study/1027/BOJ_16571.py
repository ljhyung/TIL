'''
https://www.acmicpc.net/problem/16571
알파 틱택토
골드3

'''

lst = [list(map(int, input().split())) for _ in range(3)]
player = 0
cnt0=0
cnt1=0
cnt2=0
answer = 0
for r in range(3):
    for c in range(3):
        if lst[r][c]==1:
            cnt1 += 1
        elif lst[r][c]==2:
            cnt2 += 1
        else:
            cnt0 += 1
if cnt0==9:player=1
elif cnt1>cnt2:player=2
elif cnt1==cnt2:player=1

#
# def check(r, c, temp):
#     cntR = 0
#     cntC = 0
#     cntRC = 0
#     cntCR = 0
#     for k in range(3):
#         if lst[r][k] == temp:
#             cntR += 1
#         elif lst[r][k]==2//temp:
#             cntR -= 1
#         if lst[k][c] == temp:
#             cntC += 1
#         elif lst[k][c]==2//temp:
#             cntC -= 1
#         if lst[k][k] == temp:
#             cntRC += 1
#         elif lst[k][k]==2//temp:
#             cntRC -= 1
#         if lst[k][2 - k] == temp:
#             cntCR += 1
#         elif lst[k][2 - k]==2//temp:
#             cntCR -= 1
#
#     if cntR == 2:
#         return temp
#     if cntC == 2:
#         return temp
#     if r == c and cntRC == 2:
#         return temp
#     if r + c == 2 and cntCR == 2:
#         return temp
#
#     if cntR == -2:
#         return 2 // temp
#     if cntC == -2:
#         return 2 // temp
#     if r == c and cntRC == -2:
#         return 2 // temp
#     if r + c == 2 and cntCR == -2:
#         return 2 // temp
#
#     return False
#
#
# def dfs(turn):
#     global answer
#     if answer == player: return
#     Wlst = []
#     Llst = []
#     for r in range(3):
#         for c in range(3):
#             if lst[r][c] == 0:
#                 # lst[r][c]=turn
#                 temp = check(r, c, turn)
#                 if temp == turn:
#                     Wlst.append([r, c])
#                 elif temp == 2 // turn:
#                     Llst.append([r, c])
#     if Wlst and turn == player:
#         answer = player
#         return
#     elif len(Llst)>1 and turn==player:
#         answer=2//player
#         return
#     elif Llst:
#         lst[Llst[0][0]][Llst[0][1]] = turn
#         dfs(2//turn)
#         lst[Llst[0][0]][Llst[0][1]] = 0
#     else:
#         for c in range(3):
#             for r in range(3):
#                 if lst[r][c] == 0:
#                     lst[r][c] = turn
#                     dfs(2//turn)
#                     lst[r][c] = 0
# dfs(player)
# if cnt0==9:
#     print("D")
# elif answer == 0:
#     print("D")
# elif answer == player:
#     print("W")
# else:
#     print("L")

def check():

    cntRC = 0
    cntCR = 0
    for k in range(3):
        if lst[k][k]==1:
            cntRC+=1
        elif lst[k][k]==2:
            cntRC-=1
        if lst[k][2-k]==1:
            cntCR+=1
        elif lst[k][2-k]==2:
            cntCR-=1

        cntR = 0
        cntC = 0
        for j in range(3):
            if lst[k][j]==1:
                cntR+=1
            elif lst[k][j]==2:
                cntR-=1
            if lst[j][k]==1:
                cntC+=1
            elif lst[j][k]==2:
                cntC-=1
        if cntR==3:
            return 1
        elif cntR==-3:
            return 2
        if cntC == 3:
            return 1
        elif cntC == -3:
            return 2
    if cntRC == 3:
        return 1
    elif cntRC == -3:
        return 2
    if cntCR == 3:
        return 1
    elif cntCR == -3:
        return 2
    return 0

def dfs2(depth, turn):
    if depth==cnt0:
        return 0
    tempAnswer = []
    for r in range(3):
        for c in range(3):
            if lst[r][c]==0:
                lst[r][c] = turn
                if check():
                    tempAnswer.append(turn)
                else:
                    tempAnswer.append(dfs2(depth+1,2//turn))
                lst[r][c] = 0
    # print(tempAnswer)
    if turn in tempAnswer:
        return turn
    elif 0 in tempAnswer:
        return 0
    else:
        return 2//turn

answer = dfs2(0,player)
if answer==player:
    print("W")
elif answer==2//player:
    print("L")
else:
    print("D")

