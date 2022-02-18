import sys
sys.stdin = open("input.txt", "r")


for i in range(10):
    N = int(input())
    lst = []
    r = 99
    for _ in range(100):
        lst.append(list(map(int, input().split())))
    for k in range(100):
        if lst[99][k] == 2:
            c = k               # 밑의 시작 부분
            break
    while r>0:
        r -= 1                  # 일단 한칸 올라가기
        if 0<=c-1<100 and lst[r][c-1]:          # 왼쪽 체크
            while 0<=c-1<100 and lst[r][c-1]:   # 왼쪽 끝까지 이동
                c -= 1
        elif 0<=c+1<100 and lst[r][c+1]:        # 오른쪽 체크 그냥 if로 했다가 왼쪽 이동 후 다시 오른쪽으로 이동 elif 사용
            while 0<=c+1<100 and lst[r][c+1]:   # 오른쪽 끝까지 이동
                c += 1


    print(f'#{N} {c}')

    # while True:           # delta로 하려고 했는데 왼쪽으로만 가고 그 후 오른쪽으로 가고 등 어려워서 변경
    #     if not r:
    #         result = c
    #         break
    #     else:
    #         nr = r - 1
    #         nc = c + dc[delta]
    #         if 0<=nr<100 and 0<=nc<100 and lst[nr][nc]:
    #             r, c = nr, nc                 # 이동하기 전 현재 위치를 0으로 바꾸어서 돌아가기 방지
    #         else:
    #             if delta == 0 or delat == 1:
    #                 delta = 2
    #             else:
    #                 delta = (delta + 1) % 3