import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lstw = list(map(int, input().split()))
    lstt = list(map(int, input().split()))
    lstw.sort(reverse=True)
    lstt.sort(reverse=True)
    used = [0]*M
    cnt = 0
    for k in lstw:      # 무거운 짐 순서로
        for i in range(M):
            if lstt[i]>=k and used[i]==0:   # 짐을 운반할 수 있고 아직 하지 않은 용량이 큰 트럭부터
                cnt += k
                used[i]=1
                break
    print(f'#{tc} {cnt}')   # 최적 해인지는 모르겠습니다