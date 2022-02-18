import sys
sys.stdin = open("input.txt", "r")

tc = int(input())

for i in range(tc):
    N = int(input())
    lst = list(map(int, input().split())) + [0]
    maxcnt = 0
    cnt = 1
    for j in range(1, N+1):
        if lst[j] > lst[j-1]:
            cnt += 1
        else:
            if maxcnt < cnt:
                maxcnt = cnt
            cnt = 1
    print(f'#{i+1} {maxcnt}')