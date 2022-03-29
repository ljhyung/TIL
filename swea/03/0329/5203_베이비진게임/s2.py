import sys
sys.stdin = open("input.txt", "r")


def sol(lst):
    if len(lst)>=3:
        for i in range(len(lst)-2):
            if lst[i]==lst[i+1]==lst[i+2]:
                return 1
            # if lst[i+1]-lst[i]==lst[i+2]-lst[i+1]==1: # 중복 시 체크가 안 된다
            #     return 1
            if lst[i]+1 in lst and lst[i]+2 in lst:
                return 1

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    p1 = []
    p2 = []
    res = 0
    for i in range(len(lst)//2):
        p1.append(lst[i*2])
        p1.sort()
        if sol(p1):
            res += 1
            break
        p2.append(lst[i*2+1])
        p2.sort()
        if sol(p2):
            res += 2
            break
    print(f'#{tc} {res}')