import sys
sys.stdin = open("input.txt", "r")

tc = int(input())

# binary 01, 10

for i in range(tc):
    N = int(input())
    lst = []
    check = [[0]*10 for _ in range(11)]     # 좌표를 이중 리스트로 표현
    cnt = 0
    for j in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for k in range(r1,r2+1):
            for l in range(c1, c2+1):
                check[k][l] = check[k][l] | color   # 빨강이면 01로 or, 파랑이면 10으로 or하여 같은 수가 겹쳐도 1을 유지
    for q in range(10):
        for p in range(10):
            if check[q][p] == 3:                    # 둘 다 칠해지면 이진수 11 -> 3
                cnt += 1
    print(f'#{i+1} {cnt}')
