import sys
from math import ceil

sys.stdin = open("input.txt", "r")

def findmax(lst):
    result = 0
    for i in lst:
        if result < i:
            result = i
    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    check = [0]*201             # 이동하는데 방 사이의 복도를 지나간다는 표시 체크
    for i in range(N):
        sta, en = map(int, input().split())
        if sta > en:            # 큰 방에서 작은 방으로도 고려
            sta, en = en, sta
        for k in range(ceil(sta/2), ceil((en)/2)+1):    # 1~3, 4~6도 겹치기 때문에 이를 해결하기 위해서 윗방과 아랫방 사이의 복도를 기준으로 계산
            check[k] += 1
    print(f'#{tc} {findmax(check)}')
