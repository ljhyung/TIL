import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    i = -1
    res = ''
    while N:
        if N>=2**i:
            N -= 2**i
            res += '1'
        else:
            res += '0'
        if len(res)>12:
            res = 'overflow'
            break
        i -= 1
    print(f'#{tc} {res}')