import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    for i in range(int(N**(1/3))-2,int(N**(1/3))+2):
        if i**3==N:
            res = i
            break
        else:
            res = -1
    print(f'#{tc} {res}')