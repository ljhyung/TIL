import sys
sys.stdin = open('input.txt', 'r')

tc = int(input())
for i in range(tc):
    lst = list(map(int, input()))
    check = [0] * 12    # 카운팅 정렬을 위한 리스트, tri와 run을 같이 체크하기 위해 마지막에 0 두개 추가
    check_id = 0        # 검사 기준이 되는 디폴트 인덱스 값 설정
    tri = 0
    run = 0
    for j in range(6):
        check[lst[j]] += 1
    while check_id < len(check)-2:
        if check[check_id] >= 3:    # tri부터 먼저 검사
            tri += 1
            check[check_id] -= 3
            continue                # tri가 맞으면 같은 자리에서 run도 체크하기 위해
        if check[check_id] and check[check_id+1] and check[check_id+2]:
            run += 1
            check[check_id] -= 1
            check[check_id + 1] -= 1
            check[check_id + 2] -= 1
            continue
        check_id += 1
    if run + tri == 2:
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')