import sys
sys.stdin = open('input.txt', 'r')

tc = int(input())
for i in range(tc):
    N = int(input())
    lst = list(map(int, input().split()))
    max_fall = 0
    for check in range(N):
        cnt = 0
        for j in range(check,N):        # 체크할 건물 오른쪽에 더 높은 건물이 있는지
            if lst[check] <= lst[j]:    # index가 check인 건물의 칸도 낙하하는 칸이 아니니깐 포함해서 인덱스가 0부터 시작하는 것을 메꾼다
                cnt += 1
        fall = N - check - cnt          # 전체 가로 길이에서 낙하 거리 계산
        if max_fall < fall:
            max_fall = fall             # 낙하 중 제일 큰 값 결정
    print(f'#{i+1} {max_fall}')