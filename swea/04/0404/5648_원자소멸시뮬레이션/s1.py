import sys
sys.stdin = open("input.txt", "r")

def sol():
    global res
    t=0
    while t<4002:
        if len(lst)==1:
            break
        pset = set()
        dlset = set()
        for i in range(len(lst)):
            lst[i][1] += dr[lst[i][2]]
            lst[i][0] += dc[lst[i][2]]
            if (lst[i][0], lst[i][1]) in pset:
                dlset.add((lst[i][0], lst[i][1]))
            pset.add((lst[i][0], lst[i][1]))
        if dlset:
            for i in range(len(lst)-1,-1,-1):
                if (lst[i][0],lst[i][1]) in dlset:
                    res += lst[i][3]
                    lst.pop(i)
        t += 1


dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        c,r,d,K = map(int, input().split())
        lst.append([c*2,r*2,d,K])
    res = 0
    sol()
    print(f'#{tc} {res}')