import sys
from collections import deque

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ci = list(map(int, input().split()))
    res = 0
    cold_pizza = deque()    # 요리 전 피자 큐
    hwa = deque()           # 화덕 큐

    for c in range(len(ci)):    # 냉동피자 채워넣기
        cold_pizza.append((ci[c], c+1))
    for _ in range(N):          # 화덕에 피자 넣기
        temp = cold_pizza.popleft()
        hwa.append(temp)

    while hwa:
        cicheck = hwa.popleft() # 차례 피자 꺼내서 확인
        if cicheck[0]//2 == 0:  # 치즈양 확인 후 피자 꺼냄
            if len(cold_pizza) == 0 and not hwa:    # 남은 냉동 피자가 없고 화덕이 비어서 마지막 피자일 때
                res = cicheck[1]
                break
            elif len(cold_pizza) == 0:              # 남은 냉동 피자 없고 화덕에 다른 피자가 있을 때
                continue
            else:                                   # 냉동 피자를 빈 자리에 넣기
                temp = cold_pizza.popleft()
                hwa.append((temp[0], temp[1]))
        else:                                       # 치즈가 남은 피자 치즈양 감소시키고 화덕에 넣기기
            hwa.append((cicheck[0]//2, cicheck[1]))
    print(f'#{tc} {res}')


