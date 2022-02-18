import sys
sys.stdin = open('input.txt', 'r')

tc = int(input())


for i in range(tc):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    check = [0] * (N+1)                 # 충전하는 곳을 체크할 check 리스트
    check_id = 0                        # 현 장소
    cnt = 0
    for j in range(M):
        check[lst[j]] = 1               # 충전하는 곳을 check 리스트에 표시
    while check_id <= N-K-1:            # 마지막 충전이 필요한 곳까지
        temp_check = check_id           # 충전을 하였는지 체크하기 위한 변수
        for inid in range(check_id+K, check_id, -1):    # 출발 지점에서 한번 충전으로 움직일 수 있는 k로 이동한 곳에서부터 역순으로 충전소 체크
            if check[inid]:             # 충전소가 있는지 체크
                check_id = inid         # 충전소 있는 장소를 현 장소로
                cnt += 1                # 충전 횟수 증가
                break
        if temp_check == check_id:      # k이동시에 충전할 곳이 없다면 결과값 0
            cnt = 0
            break
    print(f'#{i+1} {cnt}')


