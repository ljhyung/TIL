import sys
sys.stdin = open("input.txt", "r")

tc = int(input())

def bsearch_cnt(P, num):
    start = 1               # 처음에 1로 설정해서 실패
    end = P
    cnt = 1                 # 찾는 횟수
    while start<=end:
        md = (start+end)//2 # 중간 값 설정
        if md == num:       # 원하는 숫자 찾으면 cnt횟수 반환
            return cnt
        elif md > num:      # 중간값이 찾는 값보다 크면 끝을 중간값으로
            end = md        # md-1 로 설정해서 실패
            cnt += 1
        elif md < num:      # 중간값이 찾는 값보다 작으면 시작을 중간값으로
            start = md
            cnt += 1
    return cnt


for i in range(tc):
    P, Pa, Pb = map(int, input().split())
    a = bsearch_cnt(P, Pa)
    b = bsearch_cnt(P, Pb)
    if a<b:
        result = 'A'
    elif a>b:
        result = 'B'
    else:
        result = 0
    print(f'#{i+1} {result}')



# def bsearch_cnt(sta, end, num, cnt):
#     if num > end or sta > end:
#         return 10*10
#     if int((sta+end)/2) == num:
#         return cnt
#     elif int((sta+end)/2) > num:
#         end = int((sta+end)/2)-1
#     elif int((sta+end)/2) < num:
#         sta = int((sta+end)/2)+1
#     cnt += 1
#     return bsearch_cnt(sta, end, num, cnt)