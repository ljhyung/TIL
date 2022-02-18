import sys
sys.stdin = open("input.txt", "r")

tc = int(input())

def my_sum(lst, r, c, M):
    total = 0
    for u in range(r, r+M):
        for p in range(c, c + M):
            total += lst[u][p]
    return total

def my_max(lst):
    result = lst[0]
    for num in lst:
        if result < num:
            result = num
    return result

for i in range(tc):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    kill_list = []
    for j in range(N-M+1):
        for k in range(N-M+1):
            kill_list.append(my_sum(lst, j, k, M))
    print(f'#{i+1} {my_max(kill_list)}')