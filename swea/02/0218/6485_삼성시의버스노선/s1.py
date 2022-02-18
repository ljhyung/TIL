import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bus = [0]*5001
    for i in range(1,N+1):
        A, B = map(int, input().split())
        for k in range(A,B+1):      # 노선 시작 끝을 받아서 버스 1개 다닌다고 추가
            bus[k] += 1
    P = int(input())
    J = [0]*(P)
    for i in range(P):
        J[i] = int(input())
    print(f'#{tc}', end='')
    for i in J:
        print(f' {bus[i]}', end='')
    print()                         # 다음 케이스에 대한 줄바꿈