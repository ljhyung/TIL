import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    print(f'#{tc} {lst[M%N]}')  # %N으로 인덱스를 벗어나면 0으로 보내주기