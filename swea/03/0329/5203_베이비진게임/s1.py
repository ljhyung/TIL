import sys
sys.stdin = open("input.txt", "r")


def sol(p):
    # if p==1:
    #     if p1[-1] in p1w:
    #         return 1
    #     else:
    #         for i in range(10):
    #             if p1[i]==2:
    #                 p1w.append(i)
    #             if i<9 and p1[i] and p1[i+1]:
    #                 if 0<=i-1 and (i-1) not in p1w:
    #                     p1w.append(i-1)
    #                 if i+2<=9 and (i+2) not in p1w:
    #                     p1w.append(i+2)
    # if p==2:
    #     if p2[-1] in p2w:
    #         return 1
    #     else:
    #         for i in range(10):
    #             if p2[i]==2:
    #                 p2w.append(i)
    #             if i<9 and p2[i] and p2[i+1]:
    #                 if 0<=i-1 and (i-1) not in p2w:
    #                     p2w.append(i-1)
    #                 if i+2<=9 and (i+2) not in p2w:
    #                     p2w.append(i+2)
    if p == 1:
        if 3 in p1:
            return 1
        for i in range(8):
            if p1[i] and p1[i+1] and p1[i+2]:
                return 1
    elif p == 2:
        if 3 in p2:
            return 1
        for i in range(8):
            if p2[i] and p2[i+1] and p2[i+2]:
                return 1


T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    p1 = [0]*10
    # p1w = []
    p2 = [0]*10
    # p2w = []
    res = 0
    for i in range(len(lst)//2):
        p1[lst[i*2]] += 1
        if sol(1):
            res = 1
            break
        p2[lst[i*2+1]] += 1
        if sol(2):
            res = 2
            break
    print(f'#{tc} {res}')