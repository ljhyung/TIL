import sys
sys.stdin = open("input.txt", "r")

def sol(n):
    global result
    if n==N:    # n이 N에 도달하면 결과 체크하기
        cnt = 0
        for i in range(N):
            cnt += lst[suny[i]-1][suny[i+1]-1]
        result = min(result, cnt)
        return

    for i in range(1, N+1):
        if i not in suny:
            suny[n] = i
            sol(n+1)
            suny[n] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    suny = [0]*(N+1)        # 경로를 표시할 배열
    suny[0] = suny[N] = 1   # 처음과 마지막은 1
    result = 100*N
    sol(1)
    print(f'#{tc} {result}')