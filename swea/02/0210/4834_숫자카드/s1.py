import sys
sys.stdin = open('input.txt', 'r')

tc = int(input())


for i in range(tc):
    N = int(input())
    lst = list(map(int, input()))
    check = [0] * 10                # 각 카드의 갯수를 저장할 리스트
    max_card = 0                    # 최대 카드 갯수
    max_num = 0                     # 최대 카드 갯수의 인덱스이자 카드 숫자
    for j in range(N):              # 빈 리스트에 각 인덱스 값의 카드 갯수 추가
        check[lst[j]] += 1
    for k in range(10):
        if check[k] >= max_card:    # 카드 갯수가 많으면
            max_card = check[k]     # 값을 카드 갯수로
            max_num = k             # 인덱스를 카드 숫자로
    print(f'#{i+1} {max_num} {max_card}')